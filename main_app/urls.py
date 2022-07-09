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
    path('supplements/<int:sup_id>/add_taking/', views.add_taking, name='add_taking'),
    path('supplements/create/', views.TypeCreate.as_view(), name='type_create'),
    path('supplements/<int:sup_id>/assoc_type/<int:type_id>/', views.assoc_type, name='assoc_type'),
    path('supplements/<int:sup_id>/assoc_type/<int:type_id>/delete/', views.assoc_type_delete, name='assoc_type_delete'),
    path('types/', views.types_index, name='types_index'),
    path('types/<int:pk>/', views.TypeDetail.as_view(), name='types_detail'),
    path('types/create/', views.TypeCreate.as_view(), name='types_create'),
    path('types/<int:pk>/update/', views.TypeUpdate.as_view(), name='types_update'),
    path('types/<int:pk>/delete/', views.TypeDelete.as_view(), name='types_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]