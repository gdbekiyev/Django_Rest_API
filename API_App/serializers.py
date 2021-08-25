from rest_framework import serializers
from .models import *


class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'


class Sorag_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sorag_Type
        fields = '__all__'


class SoragSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sorag
        fields = '__all__'


class SoragSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Sorag
        fields = '__all__'
        depth = 1


class StartTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
