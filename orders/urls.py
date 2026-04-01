from django.urls import path
from .views import order_list,add_order,daily_profit,delete_order,update_order

app_name = 'orders'

urlpatterns = [
    path('add/', add_order.as_view(), name='add_order'),           
    path('', order_list.as_view(), name ='order_list') ,
    path('profit/', daily_profit.as_view(), name='daily_profit'),
    path('delete/<int:pk>/', delete_order.as_view(), name='delete_order'),
    path('update/<int:pk>/', update_order.as_view(), name='update_order')
]