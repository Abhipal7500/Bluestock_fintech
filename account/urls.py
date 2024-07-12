from django.urls import path, include
from account.views import UserResgistrationView, UserLoginView
urlpatterns = [
    path('register/', UserResgistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
