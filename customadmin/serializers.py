from rest_framework import serializers
from account.models import User
from customadmin.models import IPOInfo

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AddipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPOInfo
        fields = '__all__'        
