"""
Robusr 2026.2.2
用户评论组件序列化器
"""

from rest_framework import serializers

from stuti_app.comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"