from django.db.models import fields
from app.models import userdata1
from rest_framework import serializers

class useSerializer(serializers.ModelSerializer):
    class Meta:
        model=userdata1
        fields=['username','email','password','Address']