from django.db import models
from django.core.exceptions import ValidationError

class Customer(models.Model):
	login_id = models.CharField(max_length=20, primary_key=True, blank=False)
	name = models.CharField(max_length=50, blank=False)
	password = models.CharField(max_length=16, blank=False)
	cc_num = models.CharField(max_length=16, verbose_name="credit card number")
	address = models.CharField(max_length=100)
	phone_num = models.CharField(max_length=10)
	def __str__(self):
		return self.login_id + " " + self.name

class Book(models.Model):
	isbn = models.CharField(max_length=14, primary_key=True,blank=False)
	title = models.CharField(max_length=100, blank=False)
	authors = models.CharField(max_length=100, blank=False)
	publisher = models.CharField(max_length=100, blank=False)
	year_op = models.DateTimeField(blank=False, verbose_name="year of publication")
	copies = models.IntegerField(blank=False, verbose_name="available copies")
	price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
	url = models.CharField(max_length=100)
	book_format_choices = (
		('hc', 'hardcover'),
		('sc', 'softcover')
	)
	b_format = models.CharField(max_length=2, choices=book_format_choices)
	keywords = models.CharField(max_length=100) #store all keywords as a tuple
	subject = models.CharField(max_length=50)
	def __str__(self):
		return self.title + " " + self.isbn
	def rating(self):
		if len(self.feedback_set.all()) == 0:
			return { 'score__avg': 0 }
		return self.feedback_set.aggregate(models.Avg('score'))
	def image(self):
		return self.url or 'http://placehold.it/700x1000'

class Order(models.Model):
	# order_id = models.IntegerField(primary_key=True)
	date_time = models.DateTimeField(blank=False, verbose_name="date time of order")
	customer = models.ForeignKey("Customer")
	order_status_choices = (
		('it', 'in transit to customer'),
		('pp', 'processing payment'),
		('dc', 'delivered to customer'),
		('wh', 'in warehouse'),
		('ns', 'not submitted')
	)
	status = models.CharField(max_length=2, choices=order_status_choices)
	def __str__(self):
		return str(self.id)

class Order_book(models.Model):
	order = models.ForeignKey(Order)
	book = models.ForeignKey(Book)
	copies = models.IntegerField(blank=False, verbose_name="copies ordered")
	class Meta:
		unique_together = ('order', 'book')
	def __str__(self):
		return str(self.order.id) + " " + str(self.book)

class Feedback(models.Model):
	rater = models.ForeignKey("Customer")
	book = models.ForeignKey("Book")
	score_choices = (
		(0,0),
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		(6,6),
		(7,7),
		(8,8),
		(9,9),
		(10,10)
	)
	score = models.IntegerField(choices=score_choices)
	date_time = models.DateTimeField(auto_now_add=True, blank=False, verbose_name="date time of feedback")
	short_text = models.CharField(max_length=140)
	def usefulness(self):
		return Rating.objects.filter(ratee=self.rater,book=self.book).aggregate(models.Avg('score'))
	class Meta:
		unique_together = ("rater", "book")
	def __str__(self):
		return str(self.book) + " " + str(self.rater)

class Rating(models.Model):
	def clean(self):
		if (self.rater_id == self.ratee_id):
			raise ValidationError('rater_id == ratee_id')
		if (len(Feedback.objects.filter(rater=self.ratee, book=self.book)) > 1):
			raise ValidationError('Feedback not found')
	class Meta:
		unique_together = ("book", "rater", "ratee")
	score_choices = (
		(0,0),
		(1,1),
		(2,2)
	)
	score = models.IntegerField(choices=score_choices)
	rater = models.ForeignKey(Customer, related_name='rater')
	ratee = models.ForeignKey(Customer, related_name='ratee')
	book = models.ForeignKey(Book)
	def __str__(self):
		return str(self.score) + " " + str(self.book) + " " + str(self.rater) + " " + str(self.ratee)