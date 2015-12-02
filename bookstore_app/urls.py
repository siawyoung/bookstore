from django.conf.urls import url
from . import views
from bookstore_app.views import UserView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^books/([a-zA-Z0-9]+)/$', views.book, name='book'),
    url(r'^users/(?P<user_id>\w+)/$', UserView.as_view()),
    # url(r'^admin/book/new', views.admin_books, name='admin_books'),
    # url(r'^admin/book/update', views.admin_update, name='admin_update')
]