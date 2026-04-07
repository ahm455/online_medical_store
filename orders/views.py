from rest_framework import generics
from rest_framework.response import Response
from django.db.models.functions import TruncDate
from customers.permissions import CustomPermission
from .models import Order, OrderedItems
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .serializers import OrderSerializer, OrderedItemSerializer
from django.db.models import Sum


class CreateListOrderView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermission]


class OrderRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_id'
    queryset = Order.objects.all()
    permission_classes = [CustomPermission]

class OrderListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    queryset = OrderedItems.objects.all()
    serializer_class = OrderedItemSerializer
    permission_classes = [CustomPermission]

class OrderItemsRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    serializer_class = OrderedItemSerializer
    lookup_url_kwarg = 'order_id'
    queryset = OrderedItems.objects.all()
    permission_classes = [CustomPermission]

class AddListItemsView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    serializer_class = OrderedItemSerializer
    permission_classes = [CustomPermission]

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return OrderedItems.objects.filter(order_id=order_id)

class DailyProfitView(generics.ListAPIView):
    def get_queryset(self):
        return (
            Order.objects
            .values(date=TruncDate('created_at'))
            .annotate(total_profit=Sum('profit_amount'))
            .order_by('-date')
        )

    def list(self, request, *args, **kwargs):
        return Response(self.get_queryset())