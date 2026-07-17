from django.urls import path
from . import views

urlpatterns = [
    path('', views.hii, name='hii')
]
