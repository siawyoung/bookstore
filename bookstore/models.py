from django.db import models

class Customer(models.Model):
	login_id = models.CharField(max_length=20, primary_key=True, blank=False)
	name = models.CharField(max_length=50, blank=False)
	password = models.CharField(max_length=16, blank=False)
	cc_num = models.CharField(max_length=12, verbose_name="credit card number")
	address = models.CharField(max_length=100)
	phone_num = models.CharField(max_length=10)

class Book(models.Model):
	isbn = models.CharField(max_length=14, primary_key=True,blank=False)
	title = models.CharField(max_length=100, blank=False)
	authors = models.CharField(max_length=100, blank=False)
	publisher = models.CharField(max_length=100, blank=False)
	title = models.CharField(max_length=100, blank=False)
	year_op = models.DateTimeField(blank=False, verbose_name="year of purchase")
	copies = models.IntegerField(blank=False, verbose_name="available copies")
	price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
	book_format_choices = (
		('hc', 'hardcover'),
		('sc', 'softcover')
	)
	b_format = models.CharField(max_length=2, choices=book_format_choices)
	keywords = models.CharField(max_length=100) #store all keywords as a tuple
	subject = models.CharField(max_length=50)

class Order(models.Model):
	order_id = models.IntegerField(primary_key=True)
	date_time = models.DateTimeField(blank=False, verbose_name="date time of order")
	customer = models.ForeignKey("Customer")
	order_status_choices = (
		('it', 'in transit to customer'),
		('pp', 'processing payment'),
		('dc', 'delivered to customer'),
		('wh', 'in warehouse')
	)
	status = models.CharField(max_length=2, choices=order_status_choices)

class Order_book(models.Model):
	order = models.ForeignKey(Order)
	book = models.ForeignKey(Book)
	copies = models.IntegerField(blank=False, verbose_name="copies ordered")
	class Meta:
		unique_together = ('order', 'book')

class Feedback(models.Model):
	rater = models.ForeignKey("Customer")
	book = models.ForeignKey("Book")
	score_choices = (
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
	date_time = models.DateTimeField(blank=False, verbose_name="date time of feedback")
	short_text = models.CharField(max_length=140)
	class Meta:
		unique_together = ("login_id", "isbn")

class Rating(models.Model):
	def clean(self):
		if (self.rater_id == self.ratee_id):
			raise ValidationError('rater_id == ratee_id')
		if (len(Feedback.objects.filter(rater=self.ratee, book=self.book)) > 0)
			raise ValidationError('feedback not found')
	class Meta:
		unique_together = (book, rater, ratee)
	score_choices = (
		(0,0),
		(1,1),
		(2,2)
	)
	score = models.IntegerField(choices=score_choices)
	rater = models.ForeignKey(Customer)
	ratee = models.ForeignKey(Customer)
	book = models.ForeignKey(Book)