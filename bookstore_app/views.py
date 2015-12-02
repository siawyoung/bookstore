from django.shortcuts import render
from django.http import Http404
from django.views.generic import View
from .models import Customer
# Create your views here.

def index(req):
    # template = loader.get_template('book/index.html')
    return render(req, 'book/index.html')

def register(req):
    return render(req, 'user/register.html')

class LoginView(View):
    def get(self, req):
        return render(req, 'user/login.html')
    def post(self, req):
        """
        TODO: This is the POST endpoint for the login form
        It should redirect to / if successful
        or redirect back to login page with errors
        """
        pass

class OrderView(View):
    def get(self, req):
        """
        TODO: This is the GET endpoint for the user's cart
        @orders = localStorage
        """
        pass
    def post(self, req):
        """
        TODO: This is the POST endpoint for the user to submit his orders in the cart
        """
        pass

class BookView(View):
    def get(self, req, isbn):
        return render(req, 'book/show.html')
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

class UserView(View):
    def get(self, req, user_id):
        try:
            user = Customer.objects.get(login_id=user_id)
        except Customer.DoesNotExist:
            raise Http404("User does not exist")
        truncated_cc_num = user.cc_num[-4:]
        return render(req, 'user/show.html', {'user': user, 'truncated_cc_num': truncated_cc_num})

    def post(self, req):
        """
        TODO: This is the POST endpoint for the register form
        """
        pass

def search(req, query):
    """
    GET /books/search?=
    TODO: This is the GET endpoint for searching books
    """
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
    """
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
    pass

# def get_book_rec(isbn):
#     return 

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