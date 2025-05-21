from django.shortcuts import render
from app.models import *
from django.http import response
from rest_framework import serializers


class BookMS(serializers.ModelSerializer):
    
    def get(self,request):
        book = Book.objects.all()
        serializer = BookMS(book,many=True)
        return response(serializer.data)
    
    def post(self,request):
        serializer = BookMS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
        return response(serializer.errors)