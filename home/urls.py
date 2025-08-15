from django.urls import path
from .views import *

urlpatterns = [
    
path('', views.homepage, name='home'),  # Root URL shows homepage
]
