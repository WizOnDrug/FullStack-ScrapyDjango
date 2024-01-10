from rest_framework import serializers
from .models import Jabama

class JabamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jabama
        fields = '__all__'