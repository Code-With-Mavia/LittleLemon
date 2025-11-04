from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import MenuItem, Category, Rating, Order
from .serializers import (MenuItemSerializer, CategorySerializer, RatingSerializer,UserRegistrationSerializer, CartItemSerializer, CartSerializer, OrderSerializer)
from .permissions import IsManager, IsDeliveryCrew, IsAdminOrReadOnly
from .services import CartService
from rest_framework.views import APIView


# Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


# Category & MenuItem
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory', 'category']
    search_fields = ['title']


# Manager: update item of the day (featured)
class MenuItemFeaturedView(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, pk):
        # toggle featured for a given menuitem; manager only
        try:
            item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        # set all others to not featured
        MenuItem.objects.update(featured=False)
        item.featured = True
        item.save()
        return Response(MenuItemSerializer(item).data)


# Ratings
class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]


# Admin assigns users to Manager group
class AssignManagerView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        username = request.data.get('username')
        if not username:
            return Response({'detail': 'username required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        manager_group, _ = Group.objects.get_or_create(name='Manager')
        user.groups.add(manager_group)
        return Response({'detail': f'{username} added to Manager'})


# Manager assigns user to delivery crew
class AssignDeliveryCrewView(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request):
        username = request.data.get('username')
        if not username:
            return Response({'detail': 'username required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        crew_group, _ = Group.objects.get_or_create(name='Delivery crew')
        user.groups.add(crew_group)
        return Response({'detail': f'{username} added to Delivery crew'})


# Cart endpoints
class CartAddItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        menuitem_id = request.data.get('menuitem_id')
        quantity = int(request.data.get('quantity', 1))
        if not menuitem_id:
            return Response({'detail': 'menuitem_id required'}, status=status.HTTP_400_BAD_REQUEST)
        cart = CartService.get_or_create_cart_for_user(request.user)
        ci = CartService.add_item(cart, menuitem_id, quantity)
        return Response(CartItemSerializer(ci).data, status=status.HTTP_201_CREATED)


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = CartService.get_or_create_cart_for_user(request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartCheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = CartService.get_or_create_cart_for_user(request.user)
        if not cart.items.exists():
            return Response({'detail': 'cart empty'}, status=status.HTTP_400_BAD_REQUEST)
        order = CartService.create_order_from_cart(cart)
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


# Manager assigns order to delivery crew
class AssignOrderToCrewView(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, order_id):
        username = request.data.get('username')
        if not username:
            return Response({'detail': 'username required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return Response({'detail': 'order not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        # ensure user is delivery crew
        if not user.groups.filter(name='Delivery crew').exists():
            return Response({'detail': 'user is not delivery crew'}, status=status.HTTP_400_BAD_REQUEST)
        order.delivery_crew = user
        order.save()
        return Response({'detail': f'Order {order_id} assigned to {username}'})


# Delivery crew views
class DeliveryCrewOrdersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsDeliveryCrew]
    serializer_class = OrderSerializer

    def get_queryset(self):
        # only orders assigned to this delivery user
        return Order.objects.filter(delivery_crew=self.request.user)


class DeliveryMarkDeliveredView(APIView):
    permission_classes = [IsAuthenticated, IsDeliveryCrew]

    def post(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id, delivery_crew=request.user)
        except Order.DoesNotExist:
            return Response({'detail': 'order not found or not assigned to you'}, status=status.HTTP_404_NOT_FOUND)
        order.status = 'D'
        order.save()
        return Response({'detail': 'order marked as delivered'})


# Customer: list own orders
class CustomerOrdersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

