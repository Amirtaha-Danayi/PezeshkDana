from django.urls import path
from . import views


urlpatterns = [
    path('explanation_list/', views.ExplanationList.as_view(), name='explanation_list'),
    path('<int:pk>/', views.ExplanationDetail.as_view(), name='explanation_detail'),
    path('create_explanation/', views.create_explanation, name='create_explanation'),
    path('<int:pk>/update_explanation/', views.ExplanationUpdate.as_view(), name='explanation_update'),
    path('<int:pk>/delete_explanation/', views.ExplanationDelete.as_view(), name='explanation_delete'),
]
