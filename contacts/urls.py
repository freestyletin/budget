from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', views.AddressIndexView.as_view(), name='index'),
]
