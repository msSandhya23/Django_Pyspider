from django.shortcuts import render
from rest_framework.decorator import api_view,permission
from app.models import *
from rest_framework.response import response
from rest_framework.permission import IsAuthentication
# Create your views here.
@api_view(['GET'])
def E