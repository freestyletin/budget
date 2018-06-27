from django.urls import path

from . import views

app_name = 'transactions'
urlpatterns = [
    path('', views.TransactionListView.as_view(), name='index'),
    path('<int:pk>', views.TransactionDetailView.as_view(), name='detail'),
    path('create/', views.create_transaction, name='create'),
    path('<int:pk>/edit/', views.UpdateView.as_view(), name='edit'),
]
