from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import serializers, status, generics

from foodshop.models import Restaurant, Menu, Order

from foodshop.models import Category

from accounts.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone']

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'name', 'price','category']

class OrderSerializer(serializers.ModelSerializer):
    #price=serializers.SerializerMethodField()
    #customer = UserProfileSerializer(read_only=True)
    #menu = MenuSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ['id','restaurant', 'menu','customer','date','quantity','commentaire','statut']

   # def get_price(self):
    #    return self.price
class OrderPayView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        if order.customer != request.user:
            return Response({"message": "Forbidden operation."}, status=status.HTTP_403_FORBIDDEN)
        if order.statut != 'EN_COURS':
            return Response({"message": "Cannot pay for this order."}, status=status.HTTP_400_BAD_REQUEST)
        # Add payment processing logic here
        order.statut = 'EN_TERMINE'
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class OrderPayAllView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
   

    def post(self, request, *args, **kwargs):
        # récupère l'utilisateur authentifié
        user = request.user
        # récupère tous les ordres en cours de l'utilisateur authentifié
        orders = get_list_or_404(Order, customer=user, statut='EN_COURS')
        for order in orders:
            # met à jour le statut de chaque ordre avec "TERMINÉ"
            order.statut = 'TERMINÉ'
            order.save()
        # renvoie une réponse avec les détails de tous les ordres mis à jour
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)





class CategorySerializer(serializers.ModelSerializer):
    menus = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'menus']

    def get_menus(self, instance):
        # Le paramètre 'instance' est l'instance de la catégorie consultée.
        # Dans le cas d'une liste, cette méthode est appelée autant de fois qu'il y a
        # d'entités dans la liste

        # On applique le filtre sur notre queryset pour n'avoir que les produits actifs
        queryset = instance.menus.filter(active=True)
        # Le serializer est créé avec le queryset défini et toujours défini en tant que many=True
        serializer = MenuSerializer(queryset, many=True)
        # la propriété '.data' est le rendu de notre serializer que nous retournons ici
        return serializer.data

class ParameterSerializer(serializers.Serializer):
    product_id=serializers.IntegerField()
    quantity=serializers.IntegerField()