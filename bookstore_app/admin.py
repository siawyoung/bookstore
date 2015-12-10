from django.contrib import admin

from .models import Customer, Feedback, Rating

admin.site.register(Customer)
admin.site.register(Feedback)
admin.site.register(Rating)
