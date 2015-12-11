from django.contrib import admin

from .models import Customer, Feedback, Rating, Order, Order_book

admin.site.register(Customer)
admin.site.register(Feedback)
admin.site.register(Rating)
admin.site.register(Order)
admin.site.register(Order_book)