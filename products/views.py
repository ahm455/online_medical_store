from .models import Medicine
from django.views.generic import ListView ,CreateView 

class add_medicine(CreateView):
    model = Medicine
    fields = '__all__'

class add_stock(CreateView):
    model = Medicine
    fields = ['name','quantity']  
    template_name = "products/add_stock.html" 

class medicine_list(ListView):
    model = Medicine
