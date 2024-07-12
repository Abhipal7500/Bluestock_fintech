from rest_framework import serializers
from .models import UnverifiedUser, User
from django.core.mail import send_mail
from django.conf import settings

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UnverifiedUser
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        verification_code = self.generate_verification_code()
        validated_data['verification_code'] = verification_code
        unverified_user = UnverifiedUser.objects.create(**validated_data)
        self.send_verification_email(unverified_user)
        return unverified_user

    def send_verification_email(self, unverified_user):
        subject = 'Account Verification'
        message = f'Hi {unverified_user.first_name},\n\nYour verification code is: {unverified_user.verification_code}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [unverified_user.email], fail_silently=False)

    def generate_verification_code(self, length=6):
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']
