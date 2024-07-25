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


    
