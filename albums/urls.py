from django.urls import path

from . import views

urlpatterns = [
    path('albums', views.AlbumsListView.as_view()),
    path('albums/<int:pk>/', views.AlbumsDetailView.as_view())
]