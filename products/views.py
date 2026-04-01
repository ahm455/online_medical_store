from .models import Medicine
from django.urls import reverse_lazy
from django.views.generic import ListView ,CreateView ,UpdateView

class add_medicine(CreateView):
    model = Medicine
    fields = '__all__'

class add_stock(UpdateView):
    model = Medicine
    fields = ['name','quantity']
    template_name = "products/add_stock.html"
    success_url = reverse_lazy('products:medicine_list')
 
    def form_valid(self, form):
        added_qty = form.cleaned_data['quantity']
        form.instance.quantity = form.instance.quantity + added_qty
        return super().form_valid(form)

class medicine_list(ListView):
    model = Medicine
