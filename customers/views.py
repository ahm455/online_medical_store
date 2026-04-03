import orders
from .models import Customer
from .serializers import *
from django.views.generic import ListView ,CreateView ,UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from rest_framework import generics

class CreateListCustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    lookup_url_kwarg = 'customer_id'
    queryset = Customer.objects.all()

# class add_customer(CreateView):
#     model = Customer
#     template_name = "customers/customer_form.html"
#     success_url = reverse_lazy('customers:customer_list')
#     fields = ['name', 'age', 'phone', 'address', 'city']
#
#     def get_form(self, *args, **kwargs):
#         form = super().get_form(*args, **kwargs)
#         form.fields['username'] = forms.CharField(max_length=150, required=True)
#         form.fields['password'] = forms.CharField(widget=forms.PasswordInput, required=True)
#         return form
#
#     def form_valid(self, form):
#         username = form.cleaned_data.pop('username')
#         password = form.cleaned_data.pop('password')
#         user = User.objects.create_user(username=username, password=password)
#         form.instance.user = user
#         return super().form_valid(form)
#
