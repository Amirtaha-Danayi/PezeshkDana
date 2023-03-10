from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowHome.as_view(), name='show_home')
]