CREATE TABLE Customer (
	Login_id CHAR (20)
	Name VARCHAR(50)
	Password VARCHAR(16)
	Major_credit_card_num CHAR(16)
	Address VARCHAR (100)
	Phone_num CHAR(10)
	PRIMARY KEY (Login_id));

CREATE TABLE Books(
	ISBN CHAR(14)
	Title VARCHAR (100)
	Authors VARCHAR (100)
	Publisher VARCHAR (100)
	YOP DATE()
	Available_copies INTEGER
	Price DOUBLE(4,2)
	Format CHAR(15) CHECK (Format = ‘Hardcover’ OR Format = ‘Softcover’)
	Keywords VARCHAR (100)
	Subject VARCHAR (50)
	PRIMARY KEY (ISBN));

CREATE TABLE Orders(
	Order_id INTEGER
	Date DATE()
	Time TIME()
	login_id CHAR (10)
	Status VARCHAR(25) CHECK (Status='In transit to Customer' OR Status='Processing Payment' OR Status='Delivered to Customer' OR Status='In Warehouse')
	PRIMARY KEY (Order_id)
	FOREIGN KEY (Login_id) REFERENCES Customer ON DELETE CASCADE);

CREATE TABLE Order_book(
	ISBN CHAR(14) 
	Copies_ordered INTEGER
	Order_id INTEGER
	FOREIGN KEY (ISBN) REFERENCES Books ON DELETE CASCADE
	FOREIGN KEY (Order_id) REFERENCES Orders ON DELETE CASCADE);

CREATE TABLE Feedback(
	Login_id CHAR(10)
	ISBN CHAR(14)
	Score INTEGER CHECK (score <= 10 AND score >= 0)
	Date DATE() 
	Short_text VARCHAR(140)
	PRIMARY KEY (Login_id, ISBN)
	FOREIGN KEY (Login_id) REFERENCES Customer
	FOREIGN KEY (ISBN) REFERENCES Books);

CREATE TABLE rating( 
	Score INTEGER CHECK (Score <= 2 AND Score>=0) 
	Rater_id CHAR(10)
	Ratee_id CHAR(10) CHECK (Rater_id <> Ratee_id) 
	ISBN CHAR (14)
	PRIMARY KEY(ISBN, Rater_id, Ratee_id)
	FOREIGN KEY Rater_id REFERENCES Customer
	FOREIGN KEY (Ratee_id, ISBN) REFERENCES Feedback(Login_id, ISBN);
	
