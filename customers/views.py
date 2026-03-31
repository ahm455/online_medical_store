from django.shortcuts import render, redirect
from .models import Customer
from django.views.generic import ListView , CreateView


class add_customer(CreateView):
    model = Customer
    fields = '__all__'
    template_name = "customers/customer_form.html"

class customer_list(ListView):
    model = Customer