from django.urls import path
from products.views import (
    product_list_view, 
    product_create_view, 
    dynamic_lookup_view, 
    product_delete_view
    )

app_name = 'products'
urlpatterns = [
    path('create/', product_create_view, name="product-create"),
    path('list/', product_list_view, name="product-list"),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]