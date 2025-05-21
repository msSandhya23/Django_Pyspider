from rest_framework import Serializers
from app.models import *

class EmpModelSerializer(Serializers.ModelSerializer):
    class Meta :
        models = Emp
        fields = '__all__'