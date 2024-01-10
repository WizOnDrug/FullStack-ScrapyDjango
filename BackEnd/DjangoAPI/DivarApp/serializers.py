from rest_framework import serializers
from .models import Divar

class DivarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divar
        fields = '__all__'