from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns = [
    path('create_view/', CreateListOrderView.as_view(), name='order_list_create'),
    path('', OrderListView.as_view(), name='order_Retrieve_delete_update'),
    path('<int:order_id>/items/', AddListItemsView.as_view(), name='add_list_items'),
    path('daily-profit/', DailyProfitView.as_view(), name='daily_profit'),
    path('detail/<int:order_id>', OrderRetrieveDeleteUpdateView.as_view(), name='detail_order'),
    path('update/<int:order_id>', OrderItemsRetrieveDeleteUpdateView.as_view(), name='update_order'),
]