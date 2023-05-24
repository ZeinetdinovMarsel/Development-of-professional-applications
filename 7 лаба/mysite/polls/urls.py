from django.urls import path

from .views import (
    IndexView,
    item_list, item_update, item_delete,
    cashier_list, cashier_update, cashier_delete,
    store_list, store_update, store_delete,
    check_list, check_update, check_delete,
    sale_list, sale_update, sale_delete,
    register,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('items/', item_list, name='item_list'),
    path('items/<int:pk>/update', item_update, name='item_update'),
    path('items/<int:pk>/delete', item_delete, name='item_delete'),

    path('cashiers/', cashier_list, name='cashier_list'),
    path('cashiers/<int:pk>/update', cashier_update, name='cashier_update'),
    path('cashiers/<int:pk>/delete', cashier_delete, name='cashier_delete'),

    path('stores/', store_list, name='store_list'),
    path('stores/<int:pk>/update',store_update, name='store_update'),
    path('stores/<int:pk>/delete', store_delete, name='store_delete'),

    path('checks/', check_list, name='check_list'),
    path('checks/<int:pk>/update', check_update, name='check_update'),
    path('checks/<int:pk>/delete', check_delete, name='check_delete'),
    
    path('sales/', sale_list, name='sale_list'),
    path('sales/<int:pk>/sales', sale_update, name='sale_update'),
    path('sales/<int:pk>/delete', sale_delete, name='sale_delete'),

    path('register/', register, name='register'),
    
]
