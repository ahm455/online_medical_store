from django.urls import path
from . import views
from .views import *

app_name = 'products'

urlpatterns = [
    path('', CreateListMedicineView.as_view(), name='medicine_list_create'),
    path ('detail/<str:medicine_id>', MedicineRetrieveDeleteUpdateView.as_view(), name='medicine_delete_update'),
    ]
