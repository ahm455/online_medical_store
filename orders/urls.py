from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns = [
    path('create/', CreateListOrderView.as_view(), name='order_list_create'),
    path('', OrderListView.as_view(), name='order_list'),
    path('<int:order_id>/items/', AddItemsView.as_view(), name='add_items'),
    path('daily-profit/', DailyProfitView.as_view(), name='daily_profit'),
    path('detail/<str:order_id>', OrderDeleteUpdateView.as_view(), name='detail_customer')
]