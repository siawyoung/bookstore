import pdb
import re
import datetime
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .models import Customer, Feedback, Book, Order_book, Rating, Order
from .forms import LoginForm, RegisterForm
from .token import IssueToken, VerifyToken, DecodeToken

def statistics(req):
    pdb.set_trace()
    return render(req, 'admin/statistics.html')

def index(req):
    user = getUser(req)
    books = Book.objects.all()
    return render(req, 'book/index.html', { 'user': user, 'books': books })

class UserView(View):
    def get(self, req):
        user = getUser(req)
        if not user:
            return HttpResponseRedirect('/login/')
        truncated_cc_num = user.cc_num[-4:]

        orders = user.order_set.exclude(status='ns')
        order_books = [ Order_book.objects.filter(order=o).all() for o in orders ]
        books = [ [ (o, o.book) for o in ob ] for ob in order_books ]
        orders_information = reversed(zip(orders, books))

        feedbacks = user.feedback_set.all()
        feedbacks_books = [ f.book for f in feedbacks ]
        feedbacks_information = zip(feedbacks, feedbacks_books)

        ratings = Rating.objects.filter(rater=user)
        ratees = [ rating.ratee for rating in ratings ]
        books = [ rating.book for rating in ratings ]
        ratings_feedbacks = [ Feedback.objects.get(rater=ratee,book=book) for ratee, book in zip(ratees, books) ]
        rating_info = zip(ratings, ratees, books, ratings_feedbacks)
        return render(req, 'user/show.html', {
            'user': user,
            'truncated_cc_num': truncated_cc_num,
            'orders': orders_information,
            'feedbacks': feedbacks_information,
            'ratings': rating_info
        })

    def post(self, req):
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            response = HttpResponseRedirect('/')
            response.set_cookie('bookstore_token', IssueToken(user.login_id))
            return response
        else:
            return render(req, 'user/register.html', { 'form': form })

def register(req):
    return render(req, 'user/register.html', { 'form': RegisterForm() })

class LoginView(View):
    def get(self, req):
        return render(req, 'user/login.html', { 'form': LoginForm() })
    def post(self, req):
        username = req.POST.get('login_id', '')
        password = req.POST.get('password', '')
        try:
            user = Customer.objects.get(login_id=username, password=password)
        except Customer.DoesNotExist:
            user = None
        if user:
            response = HttpResponseRedirect('/')
            response.set_cookie('bookstore_token', IssueToken(user.login_id))
            return response
        else:
            error = 'The username or password is incorrect.'
            return render(req, 'user/login.html', { 'form': LoginForm(), 'error': error })

def add_to_cart(req, isbn):
    # pdb.set_trace()
    copies_requested = int(req.POST.get("quantity"))
    user = getUser(req)
    book = Book.objects.get(isbn=isbn)
    try:
        cart = user.order_set.filter(status='ns')[0]
    except:
        cart = Order(customer=user,status='ns', date_time=datetime.datetime.now())
        cart.save()
    try:
        order_book = cart.order_book_set.get(book=book)
    except:
        order_book = Order_book(order=cart, book=book, copies=0)
        order_book.save()

    order_book.copies += copies_requested
    book.copies -= copies_requested
    order_book.save()
    book.save()
    # copies_requested = int(req.POST.get("quantity"))
    # book.copies -= int(copies_requested)
    # book.save()
    # response = HttpResponseRedirect('/orders/')
    return HttpResponseRedirect('/orders/')

class OrderView(View):
    def get(self, req):
        user = getUser(req)
        # if not user:
        #     HttpResponseRedirect('/login/')

        orders = user.order_set.filter(status='ns')
        order_books = [ Order_book.objects.filter(order=o).all() for o in orders ]
        order_books = [ item for sublist in order_books for item in sublist ]
        books = [ o.book for o in order_books ]
        orders_information = zip(order_books, books)
        sub_price = [ x[0].copies * x[1].price for x in orders_information ]
        orders_information = zip(order_books, books, sub_price)
        grand_total = sum(sub_price)
        return render(req, 'order/index.html', { 'user': user, 'orders': orders_information, 'grand_total': grand_total })
    def post(self, req):
        user = getUser(req)
        orders = user.order_set.filter(status='ns').update(status='dc', date_time=datetime.datetime.now())
        return HttpResponseRedirect('/users/')
        """
        TODO: This is the POST endpoint for the user to submit the orders that are in the cart
        """
        pass

class BookView(View):
    def get(self, req, isbn):
        """
        Need these variables to inject into the view:
        @recommendations = book recommendations
        """
        try:
            book = Book.objects.get(isbn=isbn)
        except:
            raise Http404('This book does not exist.')
        return render_book_show(req, book, user=getUser(req))

def render_book_show(req, book, user=None, feedback_form_error=None, quantity_form_error=None):
    feedbacks = book.feedback_set.all() # not sorted yet
    feedbacks = sorted(feedbacks, key=lambda feedback: feedback.usefulness(), reverse=True)
    if not user:
        show_ratings = [ 'self' for feedback in feedbacks ]
        show_feedback_form = False
        recommendations = None
    else:
        show_ratings = [ check_if_rated_before(user, feedback) for feedback in feedbacks ]
        show_feedback_form = check_show_feedback_form(user, book)
        recommendations = None

    feedback_and_ratings = zip(feedbacks, show_ratings)
    b_format = "Hardcover" if book.b_format == 'hc' else "Softcover"
    return render(req, 'book/show.html', {
        'book': book,
        'b_format': b_format,
        'feedbacks': feedback_and_ratings,
        'show_feedback_form': show_feedback_form,
        'recommendations': recommendations,
        'feedback_form_error': feedback_form_error,
        'quantity_form_error': quantity_form_error
    })

# USING DJANGO ADMIN INSTEAD
# class AdminBookView(View):
#     def post(self, req):
#         """
#         TODO: This is the POST endpoint for the store manager to add a new book
#         """
#         pass
#     def patch(self, req):
#         """
#         TODO: This is the PATCH endpoint for the store manager to add more quantity of books
#         """
#         pass

def search(req):
    """
    GET /books/search?=
    TODO: This is the GET endpoint for searching books
    This will use the same template as GET / which is 'book/index'

    @books = books that fulfil the search query
    
    Queries are performed on the following fields:
        publisher: pub
        author: auth
        ISBN: isbn
        subject: subj
    Valid operators:
        and: __AND__ 
        or: __OR__ 
    A query string is of the form 
        q = a=A 
        or 
        q1__OP__q2

    Ordering is enforced using braces {}
    """
    def basic_query(field, value):
        query = None
        if field == "pub":
            query = Q(publisher__icontains=value)
        elif field == "auth":
            query = Q(authors__icontains=value)
        elif field == "subj":
            query = Q(subject__icontains=value)
        elif field == "title":
            query = Q(title__icontains=value)
        else:
            raise ValidationError("You search wrong")
        return query

    def get_query(string):
        query_match = re_query_capture.match(string).groupdict()
        if not query_match:
            print string
            raise ValueError("Invalid string for performing query")
            return None
        return basic_query(query_match["field"], query_match["value"])

    def combine_queries(query1, query2, operator):
        if query1 is None:
            if query2 is None:
                raise ValueError("Attempted to combine two null queries")
                return None
            return query2
        elif query2 is None:
            return query1
        if operator == OR:
            return query1 | query2
        elif operator == AND:
            return query1 & query2
        else:
            raise ValueError("Invalid operator to combine queries")

    def match_braces(string):
        starting_brace = string.find("{") 
        ending_brace = string.rfind("}")
        if starting_brace < 0 or ending_brace < 0:
            return None
        return (starting_brace, ending_brace)

    def left_to_right_collapse(string):
        if match_braces(string) != None:
            print string
            raise ValueError("Invalid query to perform left to right collapse")
            return None

        first_op_found = op_query_capture.search(string)
        if not first_op_found:
            return get_query(string)
        else:
            final_query_string = string[:first_op_found.start()]
            final_query = get_query(final_query_string)
            while first_op_found:
                first_op = first_op_found.group(0)
                next_op_found = op_query_capture.search(string, first_op_found.end())
                if not next_op_found:
                    next_query_string = string[first_op_found.end():]
                else:
                    next_query_string = string[first_op_found.end():next_op_found.start()]
                next_query = get_query(next_query_string)
                final_query = combine_queries(final_query, next_query, first_op)
                first_op_found = next_op_found
            return final_query

    AND = "__AND__"
    OR = "__OR__"
    OP_CAPTURE = r"__AND__|__OR__"
    QUERY_CAPTURE = r"(?P<field>[a-z]+)=(?P<value>.+)"
    re_query_capture = re.compile(QUERY_CAPTURE)
    op_query_capture = re.compile(OP_CAPTURE)
    search_query = req.GET.get("query")
    books = Book.objects.filter(left_to_right_collapse(search_query))
    return render(req, 'book/index.html', { 'books': books })
    pass

def create_feedback(req, book_id):
    user = getUser(req)
    if not user:
        raise Http403("Forbidden to create feedback")
    book = Book.objects.get(isbn=book_id)
    text = req.POST.get('feedback')

    if len(text) < 1 or len(text) > 140:
        error = 'The feedback is invalid. Please type between 1 and 140 characters and provide a rating.'
        return render_book_show(req, book, feedback_form_error=error)

    score = req.POST.get('score')
    feedback = Feedback(rater=user, book=book, short_text=text, score=score)
    try:
        feedback.full_clean()
        feedback.save()
        return HttpResponseRedirect('/books/' + book.isbn)
    except:
        error = 'The feedback is invalid. Please type between 1 and 140 characters and provide a rating.'
        return render_book_show(req, book, feedback_form_error=error)

def rating(req, feedback_id):
    user = getUser(req)
    feedback = Feedback.objects.get(pk=feedback_id)
    score = req.POST.get('score')
    rating = Rating(score=score, rater=user, ratee=feedback.rater, book=feedback.book)
    try:
        rating.full_clean()
        rating.save()
        return HttpResponseRedirect('/books/' + feedback.book.isbn)
    except Exception as e:
        raise Http404('The rating is invalid')

def statistics(req):
    """
    ONLY FOR STORE managers
    GET /statistics
    TODO: This is the GET endpoint for seeing the store statistics
    """
    # return render(req, 'admin/statistics.html')
    pass


########################
# HELPER FUNCTIONS
########################

def getUser(req):
    token = req.COOKIES.get('bookstore_token')
    if not token:
        return None
    if VerifyToken(token):
        return Customer.objects.get(login_id=DecodeToken(token))
    else:
        return None

def check_show_feedback_form(user, book):
    user_orders = user.order_set.exclude(status='ns')
    user_order_books = [ Order_book.objects.filter(order=o) for o in user_orders ]
    user_order_books = [item for sublist in user_order_books for item in sublist]
    all_books_ordered_by_user = [ o.book for o in user_order_books ]
    has_user_ordered_this_book = any(book == b for b in all_books_ordered_by_user)
    if has_user_ordered_this_book:
        try:
            feedback = Feedback.objects.get(rater=user, book=book)
        except Feedback.DoesNotExist:
            return True
        return False
    else:
        return False

def get_rating(user, feedback):
    return Rating.objects.get(rater=feedback.rater,book=feedback.book,ratee=user)

def check_if_rated_before(user, feedback):
    if feedback.rater == user:
        return 'self'
    try:
        rating = Rating.objects.get(rater=user,book=feedback.book,ratee=feedback.rater)
    except Rating.DoesNotExist:
        return 'no'
    if rating:
        return rating
    else:
        return 'no'

# def get_feedback():
#     pass
# class DocumentView(Resource):  
  
#     def get(self, request, document_id):  
#         if identity.is_new(document_id):  
#             form = DocumentForm()  
#         else:  
#             document = get_object_or_404(Document, pk=document_id)  
#             form = DocumentForm(document.get_values())  
  
#         model = { 'form': form, 'index_url': reverse('index') }  
#         return render_to_response('form.html', model)  
  
#     def post(self, request, document_id):  
#         if identity.is_new(document_id):  
#             document = Document()  
#         else:  
#             document = get_object_or_404(Document, pk=document_id)  
  
#         document.set_values(request.POST)  
#         document.save()  
  
#         form = DocumentForm(document.get_values())  
#         if form.is_valid():  
#             url = reverse('success', args=[document.id])  
#         else:  
#             url = reverse('document', args=[document.id])  
  

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})