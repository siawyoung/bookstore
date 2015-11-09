CREATE TABLE Customer (
	login_id CHAR (10)
	name VARCHAR(30)
	password VARCHAR(16)
	major_credit_card_num CHAR(16)
	address VARCHAR (50)
	phone_num CHAR(10)
	PRIMARY KEY (login_id))

CREATE TABLE Books(
	ISBN CHAR(14)
	Title VARCHAR (50)
	Authors VARCHAR (50)
	Publisher VARCHAR (50)
	YOP DATE()
	available_copies INTEGER
	price DOUBLE(4,2)
	Format CHAR(15) CHECK (Format = ‘Hardcover’ OR Format = ‘Softcover’)
	Keywords CHAR (20)
	Subject CHAR (20)
	PRIMARY KEY (ISBN))

CREATE TABLE orders(
	Date DATE()
	Time TIME()
	ISBN CHAR(14) 
	login_id CHAR (10)
	copies_ordered INTEGER
	status CHAR(15)
	PRIMARY KEY (login_id, ISBN, Date, Time)
	FOREIGN KEY (ISBN) REFERENCES Books ON DELETE CASCADE
	FOREIGN KEY (login_id) REFERENCES Customer ON DELETE CASCADE)

CREATE TABLE feedback(
	login_id CHAR(10)
	ISBN CHAR(14)
	score INTEGER CHECK (score <= 10 AND score >= 0)
	date DATE 
	short_text VARCHAR(100)
	PRIMARY KEY (login_id, ISBN)
	FOREIGN KEY (login_id) REFERENCES Customer
	FOREIGN KEY ISBN) REFERENCES Books)


CREATE TABLE rating( 
	Score INTEGER CHECK (Score <= 2 AND Score>=0) 
	rater_id CHAR(10)
	ratee_id CHAR(10) CHECK (rater_id <> ratee_id) 
	ISBN CHAR (14)
	PRIMARY KEY(ISBN, rater_id, ratee_id)
	FOREIGN KEY rater_id REFERENCES Customer
	FOREIGN KEY ratee_id REFERENCES Customer
	FOREIGN KEY (ISBN) REFERENCES Books)
	CONSTRAINT Rateelogin CHECK(ratee_id IN(SELECT login_id FROM feedback)) //This is not to be implemented in the SQL as this is an assertion. 
