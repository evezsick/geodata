from django.urls import path, include
from . import views

urlpatterns = [
     path("", views.index, name="id"),
     path('georgia', views.georgia, name="georgia"),
     path('paisdgales', views.paisdgales, name="paisdgales"),
 ]
