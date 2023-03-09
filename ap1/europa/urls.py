from django.urls import path, include
from . import views

urlpatterns = [
     path("", views.id, name="id"),
     path('georgia', views.georgia, name="georgia"),
     path('paisdgales', views.paisdgales, name="paisdgales"),
     path('russia2', views.russia2, name="russia2")
 ]
