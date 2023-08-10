from django.urls import path 
from . import views

urlpatterns = [
    path('list/',views.preferenceSelection),
    path('upload/',views.preferenceUpload),
]