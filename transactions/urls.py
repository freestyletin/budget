from django.urls import path

from . import views

app_name = 'transactions'
urlpatterns = [
    path('', views.TransactionListView.as_view(), name='index'),
    path('<int:pk>/', views.TransactionDetailView.as_view(), name='detail'),
    path('create/', views.create_transaction, name='create'),
    path('<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='edit'),
    path('detail', views.TransactionDetailListView.as_view(), name='detail-index'),
    path('detail/<int:pk>/', views.TransactionDetailDetailView.as_view(), name='detail-detail'),
    path('detail/create/', views.create_transaction_detail, name='detail-create'),
    path('detail/<int:pk>/edit/', views.TransactionDetailUpdateView.as_view(), name='detail-edit'),
]
