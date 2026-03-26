from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('add/', views.add_customer, name='add_customer'),
    path('list/', views.customer_list, name='customer_list'),
]