from django.urls import path
from mi.views import *
app_name = 'xyz'

urlpatterns = [
    path('captain/',captain ,name='captain'),
]

    
