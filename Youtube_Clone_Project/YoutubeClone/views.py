from django.shortcuts import render
from .models import Comments
from .serializers import CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.


class CommentsList(APIView):

    def get(self, request):
        comment = Comments.objects.all()
        serializer = CommentsSerializer(comment, many=True)
        return Response(serializer.data)
