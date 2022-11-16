from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('matches/', views.all_matches, name="all_matches"),
    path('matches/match/<int:pk>', views.one_match, name="one_match"),

]