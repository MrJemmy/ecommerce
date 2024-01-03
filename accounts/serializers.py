from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .utils import Util


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords doesn't not match")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password')


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        RefreshToken(self.token).blacklist()
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password']


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(max_length=255, required=True, style={'input_type': 'password'})

    def validate(self, attrs):
        user = self.context.get('user')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords doesn't not match")
        user.set_password(password)
        user.save()
        return attrs


class ResetPasswordLinkSerializer(serializers.Serializer):
    def validate(self, attrs):
        user = User.objects.get(email=self.context.get('user'))
        uid = urlsafe_base64_encode(force_bytes(user.id))
        print('Encoded UID : ', uid)
        token = PasswordResetTokenGenerator().make_token(user)
        print('Password Rest Token : ',token)
        link = f'http://localhost:3000/reset/{uid}/{token}/'
        print('Password Reset Link : ', link)
        data = {
            'subject': 'Reset Your Password',
            'body': link,  # make it batter.
            'to_email': user.email,
        }
        # Util.send_email(data)
        return attrs


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(max_length=255, required=True, style={'input_type': 'password'})
    def validate(self, attrs):
        try:
            uid = self.context.get('uid')
            token = self.context.get('token')

            password = attrs.get('password')
            password2 = attrs.get('password2')
            if password != password2:
                raise serializers.ValidationError("Passwords doesn't not match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Rest password token is not valid or expired")
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError(identifier)
