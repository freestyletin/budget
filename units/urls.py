from django.urls import path

from . import views

app_name = 'units'
urlpatterns = [
    path('', views.UnitIndexView.as_view(), name='index'),
    path('<int:pk>/', views.UnitDetailView.as_view(), name='detail'),
    path('create/', views.create_unit, name='create'),
    path('<int:pk>/edit/', views.UnitUpdateView.as_view(), name='edit'),
]
