from django.urls import path
from .views import *


app_name = 'customer'

urlpatterns = [
    path('', CreateListCustomerView.as_view(), name='add_List_customer'),
    path('detail/<str:customer_id>', CustomerRetrieveDeleteUpdateView.as_view(), name='detail_customer'),
]

