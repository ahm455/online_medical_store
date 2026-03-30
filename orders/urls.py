from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),              
    path('add/', views.add_order, name='add_order'),           
    path('list/', views.order_list, name='order_list'),        
    path('profit/', views.profit_report, name='profit_report') ,
    path('shipped/<int:order_id>/', views.order_shipped, name='order_shipped'),
    path('delivered/<int:order_id>/', views.order_delivered, name='order_delivered'),
]