from rest_framework import serializers
from . import models


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'avatar', 'mail', 'number',)
        model = models.Custom


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'blogger', 'title', 'content', 'created_at', 'updated_at',)
        model = models.BlogPost
