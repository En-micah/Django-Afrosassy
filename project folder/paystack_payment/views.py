from re import I
from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . import forms
from django.conf import settings
from .models import Payment
from django.contrib import messages
# Create your views here.

def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'core_shop:make-payment.html', {'payment': payment, 'paystack_secret_key': settings.PAYSTACK_SECRET_KEY })
    else:
        payment_form = forms.PaymentForm 
    return render(request, 'core_shop:initiate-payment.html', {'payment_form': payment_form})


def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'verification successful')
    else:
        messages.error(request, 'verification failed')
    return redirect('core_shop:home')