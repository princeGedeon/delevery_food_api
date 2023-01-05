from django.urls import path
from rest_framework import routers

from .views import CategoryViewset, MenuViewSet, OrderCreateView,MyOrderViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')
router.register('menu_admin',MenuViewSet,basename="menu")
router.register('my_orders',MyOrderViewSet,basename="myorder")

urlpatterns=[
    path(
        'create_order',OrderCreateView.as_view(),name="create_order"
    ),

]

urlpatterns +=router.urls