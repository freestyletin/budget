from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.AccountListView.as_view(), name='index'),
    path('<int:pk>/', views.AccountDetailView.as_view(), name='detail'),
    path('create/', views.create_account, name='create'),
    path('<int:pk>/edit/', views.AccountUpdateView.as_view(), name='edit'),
]
