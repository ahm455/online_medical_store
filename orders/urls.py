from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns =  [
    path('', OrderListView.as_view(), name='order_list'),
    path('orders/', CreateListOrderView.as_view(), name='order_create_list'),
    path('orders/<int:order_id>/', OrderRetrieveDeleteUpdateView.as_view(), name='order_detail'),
    path('orders/<int:order_id>/items/', AddListItemsView.as_view(), name='order_items_list_create'),
    path('items/<int:order_id>/', OrderItemsRetrieveDeleteUpdateView.as_view(), name='order_item_detail'),
    path('daily-profit/', DailyProfitView.as_view(), name='daily_profit'),
]