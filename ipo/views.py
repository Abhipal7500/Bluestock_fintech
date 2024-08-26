# ipo/views.py
from django.shortcuts import render

def ipo(request):
    return render(request, 'index.html')

def upcomming(request):
    return render(request, 'upcomming.html')

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

def Financials(request):
    return render(request, 'Financials.html')
    
