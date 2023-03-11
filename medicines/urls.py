from django.urls import path
from . import views


urlpatterns = [
    path('medicines_list/', views.MedicinesList.as_view(), name='medicines_list'),
    path('<int:pk>/', views.MedicinesDetail.as_view(), name='medicines_detail'),
    path('medicines_sickness/', views.create_medicines, name ='medicines_create'),
    path('<int:pk>/update_medicines/', views.MedicinesUpdate.as_view(), name = 'medicines_update'),
    path('<int:pk>/delete_medicines/', views.MedicinesDelete.as_view(), name = 'medicines_delete'),
]
