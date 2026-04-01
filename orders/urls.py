from django.urls import path
from .views import order_list,add_order,daily_profit

app_name = 'orders'

urlpatterns = [
    path('add/', add_order.as_view(), name='add_order'),           
    path('list/', order_list.as_view(), name ='order_list') ,
    path('profit/', daily_profit.as_view(), name='daily_profit')
]