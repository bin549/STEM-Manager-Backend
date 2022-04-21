from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message
from django.db.models import Q
from .serializer import MessageSerializer


class MessageAPI(APIView):

    def get(self, request, format=None):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
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

    def delete(self, request, pk, format=None):
        message = Message.objects.get(id=pk)
        message.delete()
        return Response(1)
