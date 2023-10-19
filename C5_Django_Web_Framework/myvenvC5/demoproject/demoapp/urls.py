from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
]
