from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('supplements', views.sups_index, name='index'),
    path('supplements/<int:sup_id>/', views.sups_detail, name='detail'),
]