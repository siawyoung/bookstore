"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from adminplus.sites import AdminSitePlus
from django.contrib import admin
from bookstore_app import views
import pdb

admin.site = AdminSitePlus()
admin.autodiscover()

# def get_admin_urls(urls):
#     def get_urls():
#         pdb.set_trace()
#         my_urls = patterns('', (r'^statistics/$', admin.site.admin_view(views.statistics)))
#         return my_urls + urls
#     return get_urls

# admin_urls = get_admin_urls(admin.site.get_urls())
# admin.site.get_urls = admin_urls

urlpatterns = [
	url(r'^bookstore/', include('bookstore_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('bookstore_app.urls'))
]