from django.conf.urls import url
from . import views
from bookstore_app.views import UserView, LoginView, BookView, OrderView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', LoginView.as_view()),
    url(r'^books/([a-zA-Z0-9-]+)/$', BookView.as_view()),
    url(r'^books/([a-zA-Z0-9-]+)/feedback/$', views.create_feedback, name='create_feedback'),
    url(r'^books/([a-zA-Z0-9-]+)/orders/$', views.add_to_cart, name='add_to_cart'),
    url(r'^feedback/([a-zA-Z0-9-]+)/ratings/$', views.rating, name='rating'),
    # url(r'^books/$', AdminBookView.as_view()),
    url(r'^users/$', UserView.as_view()),
    url(r'^search/+$', views.search),
    url(r'^orders/$', OrderView.as_view()),
    # url(r'addcart/$', views.add_to_cart, name='add_to_cart')
    # url(r'^admin/book/new', views.admin_books, name='admin_books'),
    # url(r'^admin/book/update', views.admin_update, name='admin_update')
]