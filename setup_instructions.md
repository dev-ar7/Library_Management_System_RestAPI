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