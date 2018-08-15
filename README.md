# django-blog
Blog built on top of django, very simple with a very bad front-end interface but it works-ish.



#Install virtual env

Install a virtual environment for the app 

#Install requirements

use pip to install all the requiremnts found on the requirements.txt in the virtual environment


#Database
The application uses sqlite db by default so you do not need to setup anything as regards to Database, 
However you will need to run:

python manage.py makemigrations
python manage.py migrate

#Create super user
After running the migrate command on the database, you will need to create a superuser to have access to the admin interface use

python manage.py createsuperuser

#Run
To run in development run 

python manage.py runserver



