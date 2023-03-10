from django.urls import path
from . import views


urlpatterns = [
    path('symptoms_list/', views.SymptomsList.as_view(), name='symptoms_list'),
    path('<int:pk>/', views.SymptomsDetail.as_view(), name='symptoms_detail'),
    path('symptoms_crete/', views.SymptomsCreate.as_view(), name='symptoms_crete'),
    path('<int:pk>/updateـsymptoms/', views.SymptomsUpdate.as_view(), name='symptoms_update'),
    path('<int:pk>/delete_symptoms', views.SymptomsDelete.as_view(), name='symptoms_delete')
]