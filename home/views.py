from django.shortcuts import render
from signin.views import firebase, auth
# Create your views here.
def index(request):
    email=request.POST.get('email')
    
    user = auth.sign_in_with_email_and_password(email, request.POST.get('pass'))

    return render(request, 'index.html', {'e':email})