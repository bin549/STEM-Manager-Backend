from rest_framework import serializers
from .models import Profile, Message


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = Profile
        fields = (
            "id",
            "name",
            "email",
            "username",
            "location",
            "short_intro",
            "bio",
            "profile_image",
            "created_time",
            "user_type",
            "get_image",
        )


class MessageSerializer(serializers.ModelSerializer):

    class Meta:

        model = Message
        fields = (
            "id",
            "sender",
            "recipient",
            "title",
            "content",
            "is_read",
            "created_time",
        )
