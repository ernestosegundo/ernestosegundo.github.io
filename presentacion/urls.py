from django.urls import path

from presentacion import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
]