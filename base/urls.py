from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path("/newUser", views.newUser, name="newUser")
]