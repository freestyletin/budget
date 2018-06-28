from django.urls import path

from . import views

app_name = 'items'
urlpatterns = [
    path('', views.ItemListView.as_view(), name='index'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('create/', views.create_item, name='create'),
    path('<int:pk>/edit/', views.ItemUpdateView.as_view(), name='edit'),
    path('generic/', views.GenericItemListView.as_view(), name='generic-index'),
    path('generic/<int:pk>/', views.GenericItemDetailView.as_view(), name='generic-detail'),
    path('generic/create/', views.create_generic_item, name='generic-create'),
    path('generic/<int:pk>/edit/', views.GenericItemUpdateView.as_view(), name='generic-edit'),
]
