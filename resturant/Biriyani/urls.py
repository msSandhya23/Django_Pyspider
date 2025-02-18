from django.urls import path
from Biriyani.views import *
app_name = 'Biriyani'

urlpatterns = [
    path("HydrabadiDumBiriyani/",HydrabadiDumBiriyani,name='HydrabadiDumBiriyani'),
    path("dumBiriyani/",dumBiriyani,name='dumBiriyani')
]
