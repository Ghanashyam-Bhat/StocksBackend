from django.urls import path 
from . import views

urlpatterns = [
    path('preference/',views.preferenceSelection),
    
]