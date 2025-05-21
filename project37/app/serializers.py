from rest_framework import Serializers
from app.models import *

class BookMS(Serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'