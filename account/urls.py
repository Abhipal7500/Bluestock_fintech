from django.urls import path
from account.views import UserRegistrationView,UserPasswordResetView, UserLoginView, VerifyEmailView,UserProfileView, SendPasswordResetEmailview

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('profile/',UserProfileView.as_view(), name='profile'),
    path('send-reset-password-email/', SendPasswordResetEmailview.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]
