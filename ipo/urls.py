from ipo import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.ipo, name='ipo'),
    path('upcomming', views.upcomming, name='upcomming'),
    path('sharkinvestor', views.sharkinvestor, name='sharkinvestor'),
    path('Allbrokers' ,views.Allbrokers, name='Allbrokers'),
    path('BrokerCompare' ,views.BrokerCompare,name='BrokerCompare'),
    path('active_clients' ,views.active_clients,name='active_clients'),
     path('charges' ,views.charges,name='charges'),
]
