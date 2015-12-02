# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import datetime

def insert_book(apps, schema_editor):
	Book = apps.get_model("bookstore_app", "Book")
	raw_data= [['978-0062294418','The Magic Strings of Frankie Presto: A Novel','Mitch Albom', 'Harper',2015,3,16.85 ,'Hardcover','Christian','Religion']
	,['978-1401312855','The Time Keeper','Mitch Albom','Hachette Books',2013,5,8.42,'Paperback','Time, Christian','Religion']
	,['978-0143125471','The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics','Daniel James Brown','Penguin Books',2014,3,9.49,'Paperback','Canoeing','Sports & Outdoors']
	,['978-1476764832','The Time Traveler"s Wife','Audrey Niffenegger', 'Scribner',2004,6, 14.28 , 'Paperback', 'Time Travel', 'Science Fiction']
	,['978-1400033805','The Closing of the Western Mind: The Rise of Faith and the Fall of Reason','Charles Freeman','Vintage', 2005, 4,13.32,'Paperback', 'Culture','Religion']
	,['978-0452299030','The Sign: The Shroud of Turin and the Secret of the Resurrection','Thomas de Wesselow','Plume',2012,10,16.00,'Hardcover','Christian','History']
	,['978-0465054725','The Magic of Math: Solving for x and Figuring Out Why','Arthur Benjamin','Basic Books',2015,2,14.84,'Hardcover','Mathematics','History']
	,['978-1848162730','Time, Space, Stars & Man: The Story of the Big Bang','Michael M. Woolfson','World Scientific Publishing Company',2009,4,83.05,'Paperback','Cosmology','Science']
	,['978-0062409850','Go Set a Watchman: A Novel','Harper Lee','Harper',2015,10, 15.00, 'Hardcover','Classics , Atticus , Scott', 'Literature']
	,['978-0446310789','To Kill a Mockingbird', 'Harper Lee','Harper',1988,2,5.15,'Paperback','Classics, Atticus, Scott','Literature']
	,['978-0743477116','Romeo and Juliet (Folger Shakespeare Library)','William Shakespeare','Simon & Schuster',2004,2,3.68,'Paperback','Classics, Plays','Literature']
	,['978-0399501487','Lord of the Flies','William Golding','Perigee Books',2003,2,6.20,'Paperback','Classics','Literature']
	,['978-0140177398','Of Mice and Men','John Steinbeck','Penguin Books',1993,8,7.00,'Paperback','Classics','Literature']
	,['978-0316346627','The Tipping Point: How Little Things Can Make a Big Difference','Malcolm Gladwell','Back Bay Books',2002,2,12.55,'Paperback','Marketing','Business, Psychology']
	,['978-0316204361','David and Goliath: Underdogs, Misfits, and the Art of Battling Giants','Malcolm Gladwell','Little, Brown and Company',2013,3,17.25,'Hardcover','Success, Underdog','Psychology']
	,['978-0316017923','Outliers: The Story of Success','Malcolm Gladwell','Little, Brown and Company',2008,5,12.42,'Hardcover','Success','Psychology']
	,['978-0374275631','Thinking, Fast and Slow','Daniel Kahneman','Farrar, Straus and Giroux',2011,3,19.23,'Hardcover','Decision-Making','Business, Psychology, Leadership']
	,['978-1594634475','Fates and Furies: A Novel','Lauren Groff','Riverhead Books',2015,6,16.77,'Hardcover','tragedy','Family Life']
	,['978-0812993547','Between the World and Me','Ta-Nehisi Coates','Spiegel & Grau',2015,6,14.40,'Hardcover','Biographies & Memoirs','Memoirs']
	,['978-0399175527','Baby Penguins Love their Mama','Melissa Guion','Philomel Books',2015,5,6.99,'Hardcover','Children"s Books','Humor']
	,['978-0060555665','The Intelligent Investor: The Definitive Book','Benjamin Graham','HarperBusiness',2015,4,13.25,'Paperback','Business & Money','Finance']
	,['978-0743200400','One Up On Wall Street','Peter Lynch','Simon & Schuster',2000,6,9.55,'Paperback','Business','Professionals & Academics']
	,['978-0316200608','The Witches: Salem, 1692','Stacy Schiff','Little, Brown and Company',2015,9,17.60,'Hardcover','Witchcraft','State & Local']
	,['978-0345542960','Tricky Twenty-Two: A Stephanie Plum Novel','Janet Evanovich','Bantam',2015,5,15.10,'Hardcover','Women Sleuths','Mystery']
	,['978-1623366322','Thug Kitchen Party Grub: For Social Motherf*ckers','Thug Kitchen','Rodale Books',2015,3,15.59,'Hardcover','Party Planning','Entertaining & Holidays']
	,['978-0833030474','A Million Random Digits with 100,000 Normal Deviates','The RAND Corporation','American Book Publishers',2001,1,54.18,'Hardcover','Mathematics','Probability & Statistics']
	,['978-1461002505','A Million Random Digits THE SEQUEL: with Perfectly Uniform Distribution','David Dubowski','CreateSpace Independent Publishing Platform',2011,8,15.95,'Hardcover','Mathematics','Probability & Statistics']
	,['978-0399536496','Images You Should Not Masturbate To','Graham Johnson','Perigee Books',2011,6,9.95,'Paperback','Humor','Love, Sex & Marriage']
	,['978-1936976027','How Not to Be a Dick: An Everyday Etiquette Guide','Meghan Doherty','Zest Books',2013,2,12.89,'Hardcover','Teens','Social Issues']
	,['978-1477468524','Unicorns Are Jerks: a coloring book exposing the cold, hard, sparkly truth','Theo Nicole Lorenz','CreateSpace Independent Publishing Platform',2015,6,6.99,'Paperback','Humor','Cold Truth']]

	for i in raw_data:
		if i[7][0]=='H':
			i[7]='hc'
		else:
			i[7]='sc'

	for bookvalues in raw_data:
		useri = Book(isbn=bookvalues[0], title=bookvalues[1], authors=bookvalues[2], publisher=bookvalues[3], year_op=str(datetime.datetime(bookvalues[4],1,1)), copies=bookvalues[5], price=bookvalues[6], b_format= bookvalues[7], keywords=bookvalues[8], subject=bookvalues[9])
		useri.save()

def insert_customer(apps, schema_editor):
	Customer = apps.get_model("bookstore_app", "Customer")
	raw_data=[['ruso61440','N. Caruso','614Bl','6144046721257440','Bloomfield, CT United States','86891563']
	,['oman2483','Wandrwoman','248319Ne','2483192448579420','New York','83078477']
	,['hris79','TChris','797T','7975291622534320','Tzer Island ','94466012']
	,['ardy46329','Jill Clardy','4632Red','4632963069597290','Redwood City, CA USA ','90279803']
	,['elge4953','Wayne Crenwelge','495Tex','4953947247797230','Texas','94106323']
	,['uBay81','William H. DuBay','812556Cou','8125569204762990','Coupeville, WA, United States ','97593078']
	,['eman30','Charles Freeman','301087E','3010874005717750','England','84447116']
	,['niel553','Ldaniel','553522La','5535225123898520','Lawrence, KS ','91148663']
	,['oner94','James Wagoner','94510S','9451077842446650','SAN FRANCISCO, CA United States','90750732']
	,['ings9871','John D. Geddings','9871col','9871767291944790','columbia, SC United States ','90490764']
	,['rios31969','Demetrios','319691V','3196911795101690','Virginia ','90549890']
	,['hlin43266','Steve Bohlin','432660Ch','4326609534498330','Chicago ','98051067']
	,['witz646','Paul Moskowitz','6462Yo','6462528689935870','Yorktown, NY','85875122']
	,['y P.337','Jerry P.','337424T','3374242119074030','Tucson, AZ United States ','90858394']
	,['Z B.6745','JUAN C. GUTIERREZ B.','674581Med','6745815452478440','Medellìn, Antioquia COLOMBIA ','97480373']
	,['kson11803','Will Errickson','118P','1180317188680790','Portland, OR United States ','98171440']
	,['aBee7020','BarbaraBee','70206F','7020645094567850','Florida','81144414']
	,['G.L.99142','G.L.','9914Bl','9914274002317940','Black Hills ','81444583']
	,['olli347','Katherine Molli','347025Mt','3470258333005800','Mt. Prospect, IL United States','81775555']
	,['nsky552','Chris Buczinsky','552391Ar','5523914431361080','Arlington Height, IL USA ','91041922']
	,['uvic31018','Linda Linguvic','3101N','3101811565486880','New York City','94021896']
	,['urci30732','Grace Furci','307325C','3073256361719190','CA USA','98775362']
	,['adit21','Ireadit','21724Chi','2172475084323540','Chicago ','99669115']
	,['sher583','Craig Fisher','5834U','5834844522243040','USA','99666936']
	,['ames750','Rick James','7504C','7504945171679000','Carolinas ','92759062']
	,['llan19','Nathan Allan','190468Pro','1904686139331080','Provo, UT USA ','89133459']
	,['hman61682','alex bushman','616829Mi','6168299749387450','Michigan ','95423799']]

	for customervalues in raw_data:
		useri = Customer(login_id=customervalues[0],name=customervalues[1],password=customervalues[2], cc_num=customervalues[3], address=customervalues[4],	phone_num=customervalues[5])
		useri.save()

def insert_feedback(apps,schema_editor):
	Feedback = apps.get_model("bookstore_app", "Feedback")
	Book = apps.get_model("bookstore_app", "Book")
	Customer = apps.get_model("bookstore_app", "Customer")
	raw_data=[['oman2483','978-0399536496', 3,'Mind over matter on this one guys, if you"re really determined, you can accomplish anything. if you can see it, you can achieve it.']
	,['hris79','978-0399536496',8,'I Came: The title of this book was very deceptive. I found each image to be uniquely arousing.']
	,['ardy46329','978-0399536496',5,'Directions unclear, got paper cuts on my dick. Would not recommend.']
	,['elge4953','978-0833030474',10,'Such a terrific reference work! But with so many terrific random digits, it"s a shame they didn"t sort them']
	,['uBay81','978-0833030474',9,'While the printed version is good, I would have expected the publisher to have an audiobook version as well. A perfect companion for one"s Ipod.']
	,['eman30','978-1461002505',2,'Lousy even for a prank gift']
	,['niel553','978-1461002505',6,'For anyone who read "A Million Random Digits," feel free to skip this book.']
	,['oner94','978-1936976027',6,'The world would be more mellow, more joyful, more productive without so many dicks ruining the calm']
	,['ings9871','978-1936976027',1,'The author is a dick']]

	for feedbackvalues in raw_data:
		useri = Feedback(rater=Customer.objects.filter(pk=feedbackvalues[0])[0],book=Book.objects.filter(pk=feedbackvalues[1])[0],score=feedbackvalues[2],short_text=feedbackvalues[3])
		useri.save()

def insert_rating(apps, schema_editor):
	Rating = apps.get_model("bookstore_app", "Rating")
	Book = apps.get_model("bookstore_app", "Book")
	Customer = apps.get_model("bookstore_app", "Customer")
	raw_data=[[2,'978-0399536496','oman2483','rios31969']
	,[2,'978-0399536496','hris79','hlin43266']
	,[2,'978-0399536496','ardy46329','witz646']
	,[2,'978-0833030474','elge4953','y P.337']
	,[2,'978-0833030474','elge4953','Z B.6745']
	,[2,'978-0833030474','uBay81', 'kson11803']
	,[2,'978-1461002505','eman30','aBee7020']
	,[2,'978-1461002505','niel553','G.L.99142']
	,[2,'978-1461002505','niel553','olli347']
	,[2,'978-1936976027','oner94','nsky552']
	,[2,'978-1936976027','ings9871','uvic31018']]

	for ratingvalues in raw_data:
		useri = Rating(score=ratingvalues[0], book=Book.objects.filter(pk=ratingvalues[1])[0], ratee=Customer.objects.filter(pk=ratingvalues[2])[0], rater=Customer.objects.filter(pk=ratingvalues[3])[0])
		useri.save()


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0003_auto_20151202_1812'),
        ('bookstore_app', '0006_auto_20151202_2358'),
    ]

    operations = [
    	migrations.RunPython(insert_book),
    	migrations.RunPython(insert_customer),
    	migrations.RunPython(insert_feedback),
    	migrations.RunPython(insert_rating)
    ]
