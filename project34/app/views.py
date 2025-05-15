from django.shortcuts import render
from app.models import School
from django.urls import path
from django.views.generic import ListView
# Create your views here.
class ListView(ListView):
    model = School
    template_name = 'home.html'
    context_object_name = 'school_list'