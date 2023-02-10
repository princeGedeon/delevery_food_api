from django.shortcuts import render, get_object_or_404
from django_filters import rest_framework as filters
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Menu, Order
from .permissions import IsHighUser
from .serializers import CategorySerializer, MenuSerializer, OrderSerializer, ParameterSerializer


# Create your views here.

class CategoryViewset(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)


class MenuViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsHighUser]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrderDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

class MyOrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('statut',)


    def get_queryset(self):

        return Order.objects.filter(customer=self.request.user.id)


class CartViewSet(viewsets.ViewSet):
    serializer_class=ParameterSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        user = request.user
        orders = Order.objects.filter(customer=user.id,statut='EN_COURS')
        print(orders)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update Profile",
        request_body=ParameterSerializer

    )
    def create(self, request):
        user = request.user
        product_id = request.data.get('product_id')
        print(product_id)
        quantity = request.data.get('quantity')
        product = get_object_or_404(Menu, pk=product_id)
        order, created = Order.objects.get_or_create(
            customer=user, menu=product, restaurant=product.restaurant,defaults={'quantity': quantity}
        )
        if not created:
            order.quantity += quantity
            order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = request.user
        order = get_object_or_404(Order, customer=user, pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class OrderCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # récupère l'utilisateur authentifié
        user = self.request.user
        # assigne l'utilisateur authentifié comme client de la commande
        serializer.validated_data['customer'] = user
        # récupère les données de la requête
        data = self.request.data
        print(data)
        # crée l'objet Order avec les données du sérializer
        serializer.save()


class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrderUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCancelView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomerOrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('customer', 'statut')

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Order.objects.filter(customer=customer_id)



