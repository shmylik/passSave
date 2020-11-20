from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test1'),
    path('ex1/', views.calculate_goods_price, name='calculate_goods_price'),
]