from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Menu, Order
from .permissions import IsHighUser
from .serializers import CategorySerializer, MenuSerializer, OrderSerializer


# Create your views here.

class CategoryViewset(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)


class MenuViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsHighUser]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MyOrderViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)



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