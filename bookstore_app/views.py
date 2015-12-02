from django.shortcuts import render
from .models import Customer
# Create your views here.

def index(req):
    # template = loader.get_template('book/index.html')
    return render(req, 'book/index.html')

def register(req):
    return render(req, 'user/register.html')

def login(req):
    return render(req, 'user/login.html')

def book(req, isbn):
    return render(req, 'book/show.html')

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