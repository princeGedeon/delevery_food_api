from django.urls import path
from rest_framework import routers

from .views import CategoryViewset, MenuViewSet, OrderCreateView

router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')
router.register('menu_admin',MenuViewSet,basename="menu")


urlpatterns=[
    path(
        'create_order',OrderCreateView.as_view(),name="create_order"
    )
]

urlpatterns +=router.urls