from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from lm_projects.models import Project, Tag, Review
from lm_users.models import Profile
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
import django.contrib.auth.password_validation as validators
from rest_framework import status
from rest_framework.response import Response

# return custom token and user info


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'email']


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'email', 'token', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        email = value
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists!")
        return value

    def validate(self, data):
        # validators.validate_password(password=data, user=User)
        # return data

        # here data has all the fields which have validated values
        # so we can create a User instance out of it
        user = User(**data)

        # get the password from the data
        password = data.get('password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=user)

        # the exception raised here is different than serializers.ValidationError
        except ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializerWithToken, self).validate(data)

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def create(self, validated_data):
        print(validated_data)
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, data):
        project = data['project']
        if data['owner'] == project.owner:
            raise serializers.ValidationError(
                "Вы не можете оценивать собственный проект")
        return data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
