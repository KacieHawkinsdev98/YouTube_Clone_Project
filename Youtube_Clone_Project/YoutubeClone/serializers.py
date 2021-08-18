from django.db.models import fields
from rest_framework import serializers
from .models import Comments

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['videoID', 'comment', 'replies', 'likes', 'dislikes']