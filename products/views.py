from .models import Medicine
from django.urls import reverse_lazy
from django.views.generic import ListView ,CreateView ,UpdateView ,DeleteView
from rest_framework import generics
from .models import Medicine
from .serializer import MedicineSerializer


class CreateListMedicineView(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicineRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicineSerializer
    lookup_url_kwarg = 'medicine_id'
    queryset = Medicine.objects.all()