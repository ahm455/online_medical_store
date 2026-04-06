import orders
from .models import Customer
from .serializers import *
from rest_framework.permissions import *
from django.views.generic import ListView ,CreateView ,UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from rest_framework import generics

class CreateListCustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    lookup_url_kwarg = 'customer_id'
    queryset = Customer.objects.all()


