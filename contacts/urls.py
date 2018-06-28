ffrom django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.ContactListView.as_view(), name='index'),
    path('<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
    path('create/', views.create_contact, name='create'),
    path('<int:pk>/edit/', views.ContactUpdateView.as_view(), name='edit'),
    path('address/', views.AddressListView.as_view(), name='address-index'),
    path('address/<int:pk>/', views.AddressDetailView.as_view(), name='address-detail'),
    path('address/create/', views.create_address, name='address-create'),
    path('address/<int:pk>/edit/', views.AddressUpdateView.as_view(), name='address-edit'),
]
