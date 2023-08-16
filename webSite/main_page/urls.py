from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='Main Page'),
    path('contuct_us/', views.contuct, name='Contact Us')
]