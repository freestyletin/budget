from django.urls import path

from . import views

app_name = 'brands'
urlpatterns = [
    path('', views.BrandListView.as_view(), name='index'),
    path('<int:pk>/', views.BrandDetailView.as_view(), name='detail'),
    path('create/', views.create_brand, name='create'),
    path('<int:pk>/edit/', views.BrandUpdateView.as_view(), name='edit'),
]
