import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'hogehoge'
#SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/todo'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = True
