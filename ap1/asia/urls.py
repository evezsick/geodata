from django.urls import path, include
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path('coreia', views.coreia, name="coreia"),
     path('japao', views.japao, name="japao"),
     path('russia', views.russia, name="russia"),
 ]
