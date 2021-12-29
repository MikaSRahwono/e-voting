from django.urls import path
from pyrebase.pyrebase import Auth
from .views import SignIn, SignUp, Authenticate
from django.urls import path

urlpatterns = [
    path('', SignIn, name='SignIn'),
    path('signup', SignUp, name='SignUp'),
    path('auth', Authenticate, name='auth')
]