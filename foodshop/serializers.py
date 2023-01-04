from rest_framework import serializers

from foodshop.models import Restaurant, Menu, Order

from foodshop.models import Category


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone']

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'name', 'price','category']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['restaurant', 'menu', 'date','quantity']




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