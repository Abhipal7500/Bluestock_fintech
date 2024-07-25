from django.urls import path
from customadmin import views
from customadmin.views import UserLoginView, ManageIPOView, DashboardView, tokenAuthenticateView

urlpatterns = [
    path('', views.adminLogin, name='admin'),
    path('adminlogin/', UserLoginView.as_view(), name='adminlogin'),
    path('manageipo/', ManageIPOView.as_view(), name='manageipo'),  # Use TemplateView
    path('dashboard/', DashboardView.as_view(), name='dashboard'),  # Use TemplateView
    path('tokenAuthenticate/', tokenAuthenticateView.as_view(), name='tokenAuthenticate'),  # Use TemplateView
]
