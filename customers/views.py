import orders
from .models import Customer
from .serializers import *
from .permissions import CustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import *
from django.views.generic import ListView ,CreateView ,UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from rest_framework import generics

class CreateListCustomerView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [CustomPermission]

class CustomerRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    serializer_class = CustomerSerializer
    lookup_url_kwarg = 'customer_id'
    queryset = Customer.objects.all()
    permission_classes = [CustomPermission]


