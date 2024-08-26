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
     path('complaints',views.complaints,name='complaints'),
     path('shareholding',views.shareholding,name='shareholding'),
     path('pros_cons',views.pros_cons,name='pros_cons'),
     path('Ratings',views.Ratings,name='Ratings'),
     path('Financials',views.Financials,name='Financials.html'),
]
