from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/', views.delete, name="delete"),
    path('edit/', views.edit_s, name="edit_s"),
    path('update/', views.update, name="update"),
]
