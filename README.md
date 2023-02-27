## MyRSPCA
MyRSPCA is a CRUD Django project that enables different RSPCAs to create accounts and add the animals they rescued to the server, so that people can adopt them. The project uses MySQL as the database management system.

#Requirements
Python 3.6 or higher
Django 3.1.7 or higher
MySQL server 5.7 or higher

#Installation

1. Clone the repository to your local machine.
	$ git clone https://github.com/your_username/MyRSPCA.git

2. Create a virtual environment and activate it.
	$ python3 -m venv env
	$ source env/bin/activate

3. Install the required packages.
	$ pip install -r requirements.txt

4. Create a MySQL database for the project.
	$ mysql -u root -p
	$ create database myrspca

5. Set up the database settings in settings.py.

python:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myrspca',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

6. Migrate the database.
	$ python3 manage.py migrate

7. Run the server.
	$ python manage.py runserver

Usage
Open your web browser and go to http://localhost:8000/.

You can add the animals that you rescued by clicking on the "Add Animal" button.

You can view, edit, and delete the animals that you added by clicking on the "My Animals" link.

People who want to adopt the animals can view them by clicking on the "Adopt" link.






