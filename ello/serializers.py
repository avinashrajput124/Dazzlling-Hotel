from dataclasses import field
from rest_framework import serializers
from ello.models import Add_Hotal

class Add_hotelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Add_Hotal
        fields='__all__'
