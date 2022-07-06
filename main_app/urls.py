from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('supplements/', views.sups_index, name='index'),
    path('supplements/<int:sup_id>/', views.sups_detail, name='detail'),
    path('supplements/create/', views.SupCreate.as_view(), name='sups_create'),
    path('supplements/<int:pk>/update/', views.SupUpdate.as_view(), name='sups_update'),
    path('supplements/<int:pk>/delete/', views.SupDelete.as_view(), name='sups_delete'),
]