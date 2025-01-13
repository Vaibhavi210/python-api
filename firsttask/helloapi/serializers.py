from rest_framework import serializers
from .models import *


class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=subject
        fields="__all__"

class userSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=user
        fields="__all__"


class marksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=marks
        fields="__all__"