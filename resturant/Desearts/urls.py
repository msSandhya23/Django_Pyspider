from django.urls import path
from Desearts.views import *
app_name = 'Desearts'

urlpatterns = [
     path("Steam/",Steam,name='Steam'),
    path("HalfSteam/",HalfSteam,name='HalfSteam'),
]
