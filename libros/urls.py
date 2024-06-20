from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('libros/', views.list, name = 'lista'),
    path('libros/<int:id>', views.detail, name = 'detalle'),
    path('libros/nuevo', views.new, name = 'nuevo'),
   
]