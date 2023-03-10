from django.urls import path
from . import views


urlpatterns = [
    path('experiments_list/', views.ExperimentsList.as_view(), name='experiments_list'),
    path('<int:pk>/', views.ExperimentsDetail.as_view(), name='experiments_detail'),
    path('experiments_create/', views.ExperimentsCreate.as_view(), name='experiments_create'),
    path('<int:pk>/experiments_update/', views.ExperimentsUpdate.as_view(), name='experiments_update'),
    path('<int:pk>/experiments_delete', views.ExperimentsDelete.as_view(), name = 'experiments_delete'),
]
