from django.shortcuts import render
import pyrebase
# Create your views here.

firebaseConfig = {
  "apiKey": "AIzaSyDEwWVDdZlXARcUrLvgEfn-goXpgpKf1nU",
  "authDomain": "e-voting-f8fd3.firebaseapp.com",
  "databaseURL": "https://e-voting-f8fd3-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "e-voting-f8fd3",
  "storageBucket": "e-voting-f8fd3.appspot.com",
  "messagingSenderId": "799413315988",
  "appId": "1:799413315988:web:c164bfd3355d96cd9c4781",
  "measurementId": "G-P2ECTV2C5Q"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

def SignIn(request):
    return render(request,"signin.html")

def SignUp(request):
    return render(request, "signup.html")

def Authenticate(request):
    return render(request, "auth.html")