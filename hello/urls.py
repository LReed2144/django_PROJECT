from django.urls import path

from . import views

#creating URL paths
urlpatterns = [
    path("", views.index, name="index"),
    #anyone's name
    path("<str:name>", views.greet, name="greet"),
    path("lyndsey", views.lyndsey, name="lyndsey")
]

