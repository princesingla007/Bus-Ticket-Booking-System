from django.urls import path
from . import views

urlpatterns = [
    path("base",views.base,name="base"),
    path("",views.index,name="index"),
    path("bus_list",views.bus_list,name="bus_list"),
    path("bus_book/<int:id>/",views.bus_book,name="bus_book"),
    path("success",views.success,name="sucess"),
    path("about",views.about,name="about"),
]
