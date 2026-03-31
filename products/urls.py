from django.urls import path
from . import views
from .views import medicine_list , add_medicine , add_stock
app_name = 'products'

urlpatterns = [ 
    path('add/', add_medicine.as_view(), name='add_medicine'),
    path('list/', medicine_list.as_view(), name='medicine_list'), 
    path('add_stock/', add_stock.as_view(), name='add_stock')  
]