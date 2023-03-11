from django.urls import path
from . import views


urlpatterns = [
    path('sickness_list/', views.SicknessList.as_view(), name='sickness_list'),
    path('<int:pk>/', views.SicknessDetail.as_view(), name='sickness_detail'),
    path('create_sickness/', views.create_sickness, name='sickness_create'),
    path('<int:pk>/update_sickness/', views.SicknessUpdate.as_view(), name='sickness_update'),
    path('<int:pk>/delete_sickness/', views.SicknessDelete.as_view(), name='sickness_delete'),
]
