from django.urls import include, path
from . import views

urlpatterns = [
    path('respond', views.custom_response, name='respond')
      
]
