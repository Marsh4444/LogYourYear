from django.urls import path
from . import views

#my urls here

urlpatterns = [
    path('', views.home, name='home'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_confirm/<int:pk>/', views.order_confirm, name='order_confirm'),
    path('complete_order/<int:pk>/', views.complete_order, name='complete_order'),
    path('edit_order/<int:pk>/', views.edit_order, name='edit_order'),
]