from django.http import Http404
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



class CommentsDetail(APIView):
    
    def get_object(self, pk):
        try:
          return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
           raise Http404     

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)


    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentsSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.update(comment, request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        comment = self.get_object(pk)
        serializer = SongSerializer(song)
        comment.delete()
        return Response(serializer.data)