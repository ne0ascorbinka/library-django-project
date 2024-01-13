from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_view, name='orders_page'),
    path('create/<int:id>', views.create_order_view, name='create_order')
]
