from django.urls import path
from csk.views import *
app_name = 'anytrhing'

urlpatterns = [
    path('captain/',captain,name='captain'),
]
