from django.urls import path
from rest_framework import routers

from .views import CategoryViewset, MenuViewSet, OrderCreateView,CartViewSet,MyOrderListView

router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')
router.register('menu_admin',MenuViewSet,basename="menu")

router.register('my_panier',CartViewSet,basename='mypanier')

urlpatterns=[
    path(
        'create_order',OrderCreateView.as_view(),name="create_order"
    ),
    path(
        'my_order_list',MyOrderListView.as_view(),name="mly_order_list"
    )

]

urlpatterns +=router.urls