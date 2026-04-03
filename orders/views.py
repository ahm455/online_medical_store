from rest_framework import generics
from rest_framework.response import Response
from django.db.models.functions import TruncDate
import orders
from .models import Order, OrderedItems
from .serializers import OrderSerializer, OrderedItemSerializer
from django.views.generic import ListView

class CreateListOrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_id'
    queryset = Order.objects.all()

class OrderListView(ListView):
    model = Order

class AddItemsView(generics.ListCreateAPIView):
    serializer_class = OrderedItemSerializer

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