from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home" ),
    path("todos/", views.todos, name="Todos"),
    path("salvar", views.salvar, name="salvar"),
    path("series", views.series, name="series")
]