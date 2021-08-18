from django.shortcuts import render
from .models import Comments
from .serializers import CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CommentsList(APIView):

    def get(self, request):
        comment = Comments.objects.all()
        serializer = CommentsSerializer(comment, many=True)
        return Response(serializer.data)

    def post (self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
