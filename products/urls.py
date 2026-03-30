from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [ 
    path('add/', views.add_medicine, name='add_medicine'),
    path('edit/<int:id>/', views.edit_medicine, name='edit_medicine'),      
    path('list/', views.medicine_list, name='medicine_list'),   
    path('add-stock/', views.add_stock, name='add_stock'),      
    path('list-stock/', views.stock_list, name='stock_list'),   
]