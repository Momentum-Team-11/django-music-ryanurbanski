from django.urls import path

from . import views

urlpatterns = [
    path('albums', views.list),
    path('albums/<int:pk>/', views.detail)
]