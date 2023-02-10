from django.urls import path
from rest_framework import routers

from .serializers import OrderPayAllView
from .views import CategoryViewset, MenuViewSet, OrderCreateView, CartViewSet, MyOrderListView, OrderUpdateView, \
    OrderCancelView, CustomerOrderListView, ProductDetailView

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
    ),
path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
path('order/cancel/<int:pk>/', OrderCancelView.as_view(), name='order-cancel'),
path('customer/orders/<int:customer_id>', CustomerOrderListView.as_view(), name='customer-orders'),
path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path("pay_to_panier/",OrderPayAllView.as_view(),name="pay_all_panier")

]

urlpatterns +=router.urls