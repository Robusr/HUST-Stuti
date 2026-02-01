"""
收藏数据序列化工具
"""
from rest_framework import serializers

from stuti_app.wants.models import Wants


class WantsSerializer(serializers.ModelSerializer):

    # 数据验证
    sku_id = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    class Meta:
        model = Wants
        fields = '__all__'
