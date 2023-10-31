from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('add_ind/', views.create_inductors, name='add_ind'),
    path('list_inds/', views.InductorsListView.as_view(), name='list_inds'),
    path('list_tests/', views.TestsListView.as_view(), name='list_tests'),
    path('list_inds/<int:pk>', views.InductorDetailView.as_view(), name='ind_detail'),
]