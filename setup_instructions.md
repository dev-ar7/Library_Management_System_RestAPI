Installation

$ git clone https://github.com/dev-ar7/Library_Management_System_RestAPI.git


$ pip install virtualenv

Then, Git clone this repo to your PC
$ https://github.com/dev-ar7/Library_Management_System_RestAPI.git

Create a virtual environment
$ virtualenv .venv && source .venv/bin/activate

Install dependancies
$ pip install -r requirements.txt

Make migrations & migrate
$ python manage.py makemigrations && python manage.py migrate

Create Super user
$ python manage.py createsuperuser

Launching the app
$ python manage.py runserver


## Endpoints  Instruction 

#### API Documentation Instruction
Method | Endpoint | Functionanlity
--- | --- | ---
GET | `/api/v1/swagger/` | API Documentation

#### Jwt token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/api/v1/token_auth/` | Request jwt token

#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/v1/auth/current_user/` | Current users
POST | `/api/v1/auth/user/create` | Creates a user

#### Author Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/v1/library/authors` | List Authors
POST | `/api/v1/library/author/create` | Creates a author
GET | `/api/v1/library/author/detail/{pk}/` | Retrieve a author
PUT | `/api/v1/library/author/update/{pk}/` | Edit a author
DELETE | `/api/v1/library/author/delete/{pk}/` | Delete a author

#### Book Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/v1/library/books/` | List Books
POST | `/api/v1/library/book/create` | Creates a book
GET | `/api/v1/library/book/detail/{pk}/` | Retrieve a book
PUT | `/api/v1/library/book/update/{pk}/` | Edit a book
DELETE | `/api/v1/library/book/delete/{pk}/` | Delete a book

#### BorrowBooks Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/v1/library/borrow_books/` | List Borrowed Books
POST | `/api/v1/library/borrow_book/create` | Creates a BorrowBook
GET | `/api/v1/library/borrow_book/detail/{pk}/` | Retrieve a BorrowBook
PUT | `/api/v1/library/borrow_book/update/{pk}/` | Edit a BorrowBook
DELETE | `/api/v1/library/borrow_book/delete/{pk}/` | Delete a BorrowBook
GET | `/api/v1/library/borrow_book/request` | Retrieve all BorrowBook requests of autheticated user
PUT | `/api/v1/library/borrow_book/request_status/update/{pk}/` | Update BorrowBook rquest status to either accepted or rejected
PUT | `/api/v1/library/borrow_book/status/{pk}/` | Update BorrowBook status either to taken or returned
