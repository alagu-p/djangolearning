from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

# app_name = 'authentication'
urlpatterns = [
    path('/user/', RegistrationAPIView.as_view()),
    path('/users/login/', LoginAPIView.as_view()),
    path('users', RegistrationAPIView.as_view()),
]
