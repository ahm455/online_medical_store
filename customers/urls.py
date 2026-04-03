from django.urls import path
from .views import *

app_name = 'customer'

urlpatterns = [
    path('', CreateListCustomerView.as_view(), name='add_customer'),
    path('detail/<str:customer_id>', CustomerDeleteUpdateView.as_view(), name='detail_customer')
]
# urlpatterns = [
#     path('add/', add_customer.as_view(), name='add_customer'),
#     path('list/', customer_list.as_view(), name='customer_list'),
#     path('delete/<int:pk>/', delete_customer.as_view(), name='delete_customer'),
#     path('update/<int:pk>/', update_customer.as_view(), name='update_customer')
# ]