from django.urls import path
from .views import *


app_name = 'customer'

urlpatterns = [
    path('', CreateListCustomerView.as_view(), name='customer_list_create'),
    path('<str:customer_id>/', CustomerRetrieveDeleteUpdateView.as_view(), name='customer_detail'),
]

