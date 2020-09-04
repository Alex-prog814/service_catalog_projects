from django.urls import path

from .views import (ItemsListView, ItemDetailsView, AddItemView, UpdateItemView, DeleteItemView)

urlpatterns = [
    # path('', ItemsListView.as_view(), name='items-list'),
    path('', ItemsListView.as_view(), name='items-list'),
    path('<int:pk>/', ItemDetailsView.as_view(), name='item-details'),
    path('add/', AddItemView.as_view(), name='add-item'),
    path('update/<int:pk>/', UpdateItemView.as_view(), name='update-item'),
    path('delete/<int:pk>/', DeleteItemView.as_view(), name='delete-item'),
]