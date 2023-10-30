from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('add_ind/', views.create_inductors, name='add_ind'),
    path('list_inds/', views.InductorsListView.as_view(), name='list_inds'),
]