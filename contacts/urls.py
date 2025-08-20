from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_create, name='contact_create'),
    path('messages/', views.contact_list, name='contact_list'),
]
