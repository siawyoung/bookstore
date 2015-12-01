from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext,loader
from .models import Customer

TEST_TEMPLATE = loader.get_template("test.html")
def index(request):
	global TEST_TEMPLATE
	context = RequestContext(request,{
		"message": "Hello world",
		})
	return HttpResponse(template.render(context))

def customerNew(request):
	global TEST_TEMPLATE
	login_id = request.post["login_id"]
	name = request.post["name"]
	password = request.post["password"]
	cc_num = request.post["cc_num"]
	address = request.post["address"]
	phone_num = request.post["phone_num"]
	
	context = RequestContext()
	return HttpResponse(template.render(context))

def customerRecord(request):
	global TEST_TEMPLATE
	return HttpResponse(template.render(context))

def bookNew(request):
	global TEST_TEMPLATE
	return HttpResponse(template.render(context))

def bookInfo(request):
	return HttpResponse(template.render(context))

def bookUpdate(request):
	global TEST_TEMPLATE
	return HttpResponse(template.render(context))

def bookSearch(request):
	global TEST_TEMPLATE
	return HttpResponse(template.render(context))

def orderNew(request):
	global TEST_TEMPLATE
	return HttpResponse(template.render(context))

def feedbackNew(request):
	global TEST_TEMPLATE
	return HttpResponse(template.render(context))

def ratingNew(request):
	global TEST_TEMPLATE
	return HttpResponse(template.render(context))
