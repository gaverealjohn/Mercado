from rest_framework import viewsets, permissions

from .models import (Cart, CartItem, Category, OrderDetail, OrderItem, PaymentDetail, Product, ProductReview)
from .serializers import (CartItemSerializer, CartSerializer, CategorySerializer, OrderDetailSerializer, OrderItemSerializer, PaymentDetailSerializer, ProductSerializer, ProductReviewSerializer)
from accounts.permissions import IsOwnerOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        """
        This view will only return the cart 
        of the user logged in.
        """
        user = self.request.user
        return Cart.objects.filter(user=user)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    

class PaymentDetailViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentDetailSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        """
        This view will only return the order details
        of the user logged in.
        """
        user = self.request.user
        return OrderDetail.objects.filter(user=user)

    
class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer