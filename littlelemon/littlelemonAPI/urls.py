from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/feature', views.MenuItemFeaturedView.as_view()),
    path('ratings', views.RatingsView.as_view()),

    # role management
    path('assign-manager/', views.AssignManagerView.as_view()),
    path('assign-delivery-crew/', views.AssignDeliveryCrewView.as_view()),

    # cart
    path('cart/', views.CartView.as_view()),
    path('cart/add', views.CartAddItemView.as_view()),
    path('cart/checkout', views.CartCheckoutView.as_view()),

    # orders
    path('orders/assign/<int:order_id>/', views.AssignOrderToCrewView.as_view()),
    path('orders/my/', views.CustomerOrdersView.as_view()),

    # delivery crew
    path('delivery/orders/', views.DeliveryCrewOrdersView.as_view()),
    path('delivery/orders/<int:order_id>/delivered/', views.DeliveryMarkDeliveredView.as_view()),
]