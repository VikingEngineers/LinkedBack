from rest_framework import serializers
from lm_projects.models import Project, Tag, Review
from lm_users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Profile
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)

    class Meta:
        model = Review
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    # owner = ProfileSerializer(many=False)
    # tags = TagSerializer(many=True)
    # reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'
