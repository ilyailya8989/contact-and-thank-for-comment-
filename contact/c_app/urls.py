from django.urls import path

from c_app import views

urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('sps/', views.sps_view, name='sps'),
]