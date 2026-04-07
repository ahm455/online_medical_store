from rest_framework import generics
from .models import Medicine
from .serializer import MedicineSerializer
from customers.permissions import CustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class CreateListMedicineView(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [CustomPermission]

class MedicineRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicineSerializer
    lookup_url_kwarg = 'medicine_id'
    queryset = Medicine.objects.all()
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [CustomPermission]