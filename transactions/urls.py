from django.urls import path

from . import views

app_name = 'transactions'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<transaction_id>/edit/', views.edit_template, name='edit'),
]
