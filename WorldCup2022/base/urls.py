from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('matches', views.match, name="matches"),

]