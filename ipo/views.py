# ipo/views.py
from multiprocessing import context
from .models import IPOInfo
from django.shortcuts import render
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.models import User
from rest_framework.response import Response
def ipo(request):
    return render(request, 'index.html')

def upcomming(request):
    upcomming = IPOInfo.objects.all()
    context={
               'upcomming' : upcomming
    }
    return render(request, 'upcomming.html', context)

def sharkinvestor(request):
    return render(request,'sharkinvestor.html')

def Allbrokers(request):
    return render(request,'Allbrokers.html')

def BrokerCompare(request):
    return render(request, 'BrokerCompare.html')

def active_clients(request):
    return render(request, 'active_clients.html')

def charges(request):
    return render(request, 'charges.html')

def complaints(request):
    return render(request, 'complaints.html')

def shareholding(request):
    return render(request, 'shareholding.html')

def pros_cons(request):
    return render( request, 'pros_cons.html')

def Ratings(request):
    return render( request , 'Ratings.html')
    
def loginuser(request):
    return render(request, 'loginuser.html')    

def createaccount(request):
    return render(request, 'createaccount.html')   

def verifyemail(request):
    return render(request, 'verifyemail.html')  

def forgotpass(request):
    return render(request, 'forgotpass.html')  

def Newpass(request, uid, token, format=None):
    try:
        id = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            return render(request, 'Newpass.html', {'error': 'Token is not valid or expired'})
        
        return render(request, 'Newpass.html')
    
    except (DjangoUnicodeDecodeError, User.DoesNotExist):
        return render(request, 'Newpass.html', {'error': 'Token is not valid or expired'})
