import pdb
from django.contrib import admin
from django.shortcuts import render
import datetime
from collections import defaultdict
from .models import Customer, Rating, Feedback, Book, Order, Order_book

def statistics(req):

    # we run a query on the Orders table
    # first, exclude orders that are not submitted yet (ns)
    # then, we filter by those having a date_time lesser than today and greater than 30 days in the past
    orders = Order.objects.exclude(status='ns').filter(date_time__lte=datetime.datetime.today(), date_time__gt=datetime.datetime.today()-datetime.timedelta(days=30))

    # then, we find all the order_books that correspond to the orders above and flatten the nested list into a flat list
    order_books = [ Order_book.objects.filter(order=o).all() for o in orders ]
    flattened_order_books = [ item for sublist in order_books for item in sublist ]

    # then, for each of the order_book, we iterate through them and aggregate their number of copies
    # so that we can find out which are the most popular ones
    most_popular_books = defaultdict(int)
    for order_book in flattened_order_books:
        most_popular_books[order_book.book.isbn] += order_book.copies

    # sort by number of copies
    most_popular_books = sorted(most_popular_books.items(), key = lambda k_v: k_v[1], reverse=True)
    most_popular_books = [ (Book.objects.get(isbn=k), v) for k,v in most_popular_books ]

    # to find the most popular authors, we do the same thing as above, except that we aggregate by author
    most_popular_authors = defaultdict(int)
    for book, number in most_popular_books:
        author = book.authors
        most_popular_authors[author] += number

    most_popular_authors = sorted(most_popular_authors.items(), key = lambda k_v: k_v[1], reverse=True)

    # likewise, for publishers
    most_popular_publishers = defaultdict(int)
    for book, number in most_popular_books:
        publisher = book.publisher
        most_popular_publishers[publisher] += number

    most_popular_publishers = sorted(most_popular_publishers.items(), key = lambda k_v: k_v[1], reverse=True)

    return render(req, 'admin/statistics.html', {
        'today_date': datetime.datetime.today().date(),
        'last_30_date': (datetime.datetime.today()-datetime.timedelta(days=30)).date(),
        'orders': orders,
        'most_popular_books': most_popular_books,
        'most_popular_authors': most_popular_authors,
        'most_popular_publishers': most_popular_publishers
    })

admin.site.register_view('statistics/', view=statistics)

admin.site.register(Customer)
admin.site.register(Feedback)
admin.site.register(Book)
admin.site.register(Rating)
