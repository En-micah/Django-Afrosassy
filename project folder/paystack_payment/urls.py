from django.urls import path
from . import views

app_name = 'paystack_payment'

urlpatterns = [
    # path('initiate_payment/', views.initiate_payment, name= 'initiate-payment'),
    path('<str:ref>/', views.verify_payment, name= 'verify-payment')          
               ]