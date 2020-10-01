from django.test import TestCase
from .models import *
from AdminPage.dbfunctions.MyUserFunc import *

# Create your tests here.

def read_all_users():
    u = MyUser.objects.all()
    for us in u:
        print(us.username)
        print(us.first_name)
        print(us.last_name)
        print(us.email)
        print(us.password)

read_all_users()