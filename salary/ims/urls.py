from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.ImsHome),

    path('addUnit/', views.CreateUnit),
    path('updateUnit/<int:pk>', views.UpdateUnit),
    path('deleteUnit/<int:pk>', views.deleteUnit),

    path('addItem/', views.CreateItem),
    path('updateItem/<int:pk>', views.UpdateItem),
    path('deleteItem/<int:pk>', views.deleteItem),

    path('addItemType/', views.CreateItemType),
    path('updateItemType/<int:pk>', views.UpdateItemType),
    path('stockItemType/<int:pk>', views.StockItemType),
    path('stockOutItemType/<int:pk>', views.StockOutItemType),
    path('productDetails/<int:pk>', views.ItemTypeDetails),
    path('deleteItemType/<int:pk>', views.deleteItemType),

    path('addInvoice/', views.CreateInvoice),
]
