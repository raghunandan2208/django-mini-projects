from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage),
    path('validate', views.validateuser, name="validate_login"),
    path('validate_otp', views.validateOTP, name="validate_otp"),
]
