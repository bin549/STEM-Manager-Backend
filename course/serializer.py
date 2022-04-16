from rest_framework import serializers
from .models import Entity


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = (
            "id",
            "title",
            "description",
            "cover_img",
            "created_time",
            "owner",
            "genre",
            "is_visible",
            "get_absolute_url",
            "get_image",
            "get_student_url",
            "serial_number",
        )
