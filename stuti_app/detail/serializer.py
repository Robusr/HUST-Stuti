"""
Robusr 2026.2.2
用户详情信息组件序列化器
"""
from rest_framework import serializers

from stuti_app.detail.models import UserDetail
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = "__all__"