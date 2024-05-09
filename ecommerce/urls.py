from django.urls import path
from .views import home, product_detail, store, filtering_view, search_product, card_view, add_to_card, delete_card, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('store/', store, name='store'),
    path('filter/<str:name>/', filtering_view, name='filtering_items'),
    path('search/', search_product, name='search_product'),
    path('card/', card_view, name='card'),
    path('add_to_card/<int:pk>/', add_to_card, name='add_to_card'),
    path('delete/card/<int:id>/', delete_card, name='delete_card'),
    path('dashboard/', dashboard, name='dashboard')
]