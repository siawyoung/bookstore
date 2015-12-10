import pdb
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .models import Customer, Feedback, Book, Order_book, Rating
from .forms import LoginForm, RegisterForm
from .token import IssueToken, VerifyToken, DecodeToken

def index(req):
    user = getUser(req)
    books = Book.objects.all()
    return render(req, 'book/index.html', { 'user': user, 'books': books })

class UserView(View):
    def get(self, req):
        user = getUser(req)
        if not user:
            HttpResponseRedirect('/login/')
        truncated_cc_num = user.cc_num[-4:]

        orders = user.order_set.all()
        order_books = [ Order_book.objects.get(order=o) for o in orders ]
        books = [ o.book for o in order_books ]
        orders_information = zip(orders, order_books, books)

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

class OrderView(View):
    def get(self, req):
        """
        TODO: This is the GET endpoint for the user's cart
        @orders = localStorage
        """
        orders = None
        # return render(req, 'order/index.html', { 'orders': orders })
        pass
    def post(self, req):
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

class AdminBookView(View):
    def post(self, req):
        """
        TODO: This is the POST endpoint for the store manager to add a new book
        """
        pass
    def patch(self, req):
        """
        TODO: This is the PATCH endpoint for the store manager to add more quantity of books
        """
        pass

def search(req, query):
    """
    GET /books/search?=
    TODO: This is the GET endpoint for searching books
    This will use the same template as GET / which is 'book/index'

    @books = books that fulfil the search query
    """
    books = None
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
    user_orders = user.order_set.all()
    user_order_books = [ Order_book.objects.get(order=o) for o in user_orders ]
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