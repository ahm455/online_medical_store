from django.urls import path
from . import views
from .views import *

app_name = 'products'

urlpatterns = [
    path('', CreateMedicineView.as_view(), name='medicine_list_create'),
    path ('detail/<str:medicine_id>', MedicineDeleteUpdateView.as_view(), name='medicine_delete_update'),
    ]




# urlpatterns = [
#     path('add/', add_medicine.as_view(), name='add_medicine'),
#     path('list/', medicine_list.as_view(), name='medicine_list'),
#     path('add-stock/<int:pk>/', add_stock.as_view(), name='add_stock'),
#     path('delete/<int:pk>/', delete_medicine.as_view(), name='delete_medicine'),
# ]