
from django.urls import path
from account.views import UserRegistrationView,UserPasswordResetView,SendPasswordRequestEmailView,UserLoginView,UserProfileView,UserChangePasswordView
urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('profile/',UserProfileView.as_view(), name='profile'),
    path('changepswd/',UserChangePasswordView.as_view(), name='changepswd'),
    path('send-reset-pswd-email/',SendPasswordRequestEmailView.as_view(), name='SendPasswordRequestEmailView'),
    path('reset-pswd/<uid>/<token>/',UserPasswordResetView.as_view(), name='UserPasswordResetView'),
]