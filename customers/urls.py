from django.urls import path
from . import views
from .views import customer_list ,add_customer

app_name = 'customers'

urlpatterns = [
    path('add/', add_customer.as_view(), name='add_customer'),
    path('list/', customer_list.as_view(), name='customer_list'),
]