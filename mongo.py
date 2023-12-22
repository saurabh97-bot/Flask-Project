import mongoengine.errors
from flask import Flask
from mongoengine import Document,StringField,connect,EmailField
from mongoengine.errors import NotUniqueError

app = Flask(__name__)


db = "mydatabase"
host = "127.0.0.1"
port = 27017


connect(db=db,host=host,port=port)


class Post(Document):
    title = StringField(required=True,unique=True)
    description = StringField()

new_post = Post(title='Sample Post',description='This is my Post')
new_post.save()


class User(Document):
    email = EmailField(required=True, unique=True)
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)

try:
    new_users_data = [
        User(email='Ruanika@gmail.com', first_name='Ruanika', last_name='Dhawan'),
        User(email='Gautam97@gmail.com', first_name='Gautam', last_name='Veer'),
        User(email='Rakesh889@example.com', first_name='Rakesh', last_name='Dhurve'),
    ]
    User.objects.insert(new_users_data)
except NotUniqueError as e:
    print('Email Already Exists!')
