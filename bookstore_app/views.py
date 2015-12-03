import pdb
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .models import Customer, Feedback, Book
from .forms import LoginForm, RegisterForm
from .token import IssueToken, VerifyToken, DecodeToken

def getUser(req):
    token = req.COOKIES.get('bookstore_token')
    if not token:
        return None
    if VerifyToken(token):
        return Customer.objects.get(login_id=DecodeToken(token))
    else:
        return None

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

        """
        Need these variables to inject into the view:
        @orders (all of user's orders)
        @feedback (all of the user's feedback)
        @ratings (all of the user's ratings and their associated feedback)
        """
        orders = user.order_set.all()
        feedbacks = user.feedback_set.all()
        ratings = None

        return render(req, 'user/show.html', {
            'user': user,
            'truncated_cc_num': truncated_cc_num,
            'orders': orders,
            'feedbacks': feedbacks,
            'ratings': ratings
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
        @feedback = feedback belonging to the book, ranked according to usefulness
        @show_feedback_form = Boolean to check if the form should be shown
        @recommendations = book recommendations
        """
        try:
            book = Book.objects.get(isbn=isbn)
        except:
            raise Http404('This book does not exist.')
        return render_book_show(req, book)

def render_book_show(req, book, feedback_form_error=None, quantity_form_error=None):
    user_feedback = 
    feedbacks = book.feedback_set.all() # not sorted yet
    show_feedback_form = None
    recommendations = None
    b_format = "Hardcover" if book.b_format == 'hc' else "Softcover"
    return render(req, 'book/show.html', {
        'book': book,
        'b_format': b_format,
        'feedbacks': feedbacks,
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
    """
    POST /books/:book_id/feedback
    TODO: This is the POST endpoint for creating a feedback of a book
    This should check if the user has already bought a book/created a feedback for this book
    """
    pass

def feedback(req, feedback_id):
    """
    GET /feedback/:feedback_id
    TODO: This is the GET endpoint for individual feedback
    This should check if the user has already rated this feedback
    @feedback = feedback object itself
    @rating = user's rating of the feedback, if any
    """
    # feedback = Feedback.objects.get(pk: feedback_id)
    # return render(req, 'feedback/show.html', { 'feedback': feedback })
    pass

def rating(req, feedback_id):
    """
    POST /feedback/:feedback_id/ratings
    TODO: This is the POST endpoint for creating a rating of a feedback
    """
    pass

def statistics(req):
    """
    ONLY FOR STORE managers
    GET /statistics
    TODO: This is the GET endpoint for seeing the store statistics
    """
    # return render(req, 'admin/statistics.html')
    pass


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
  



# def lol(req):
#     return HttpResponse("lol")

# def lol2(req, id):
#     response = "Hi %s"
#     return HttpResponse(response % id)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})