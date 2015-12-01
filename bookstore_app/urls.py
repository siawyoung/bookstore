from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^admin/book/new', views.bookNew, name='new book'),
	url(r'^admin/book/update', views.bookUpdate, name='book update'),
	url(r'^book/(?P<book_id>[0-9]+)', views.bookInfo, name='book info'),
	url(r'^book/(?P<book_id>[0-9]+)/feedback/new', views.feedbackNew, name='new feedback'),
	url(r'^book/(?P<book_id>[0-9]+)/feedback/(?P<feedback_id>[0-9]+/rating/new)', views.ratingNew, name='new rating'),
	url(r'^book/search', views.bookSearch, name='book search'),
	url(r'^customer/new', views.customerNew, name='new customer'),
	url(r'^customer/record', views.customerRecord, name='customer record'),
	url(r'^order/new', views.orderNew, name='new order'),
]