from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Entity
from django.db.models import Q
from .serializer import CourseSerializer


class CourseAPI(APIView):

    def get(self, request, format=None):
        courses = Entity.objects.all()
        serializer = CourseSerializer(courses, many=True)
        obj = {}
        data = {}
        data["data"] = serializer.data
        data["limit"] = 20
        data["page"] = 1
        data["total"] = len(serializer.data)
        obj["data"] = data
        obj["code"] = 2000
        obj["msg"] = "success"
        return Response(obj)

    def post(self, request, format=None):

        return Response(1)

    def put(self, request, format=None):
        return Response(1)

    def delete(self, request, pk, format=None):

        print(pk)
        return Response(1)
