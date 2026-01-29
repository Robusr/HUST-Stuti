"""
Robusr 2026.1.29
前端序列化器
"""

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . import models

class AccountSerializer(ModelSerializer):
    """用户登录信息模型序列化器"""
    username = serializers.CharField(read_only=True)
    # read_only不允许前端修改
    # 显式定义 username 字段为只读

    class Meta:
        model = models.Account # 关联的模型是 Account
        fields = ["id", "username"]
        # fields = ["id", "username", "create_time"]
        # fields = "__all__" # 序列化模型的所有字段
        # 密码字段为只写（仅接受前端输入，不返回给后端）
        extra_kwargs = {
            "password": {"write_only": True}
        }

    # #补充密码验证逻辑
    # def validate_password(self, value):
    #     """验证密码长度，避免过短"""
    #     if len(value) < 6:
    #         raise serializers.ValidationError("密码长度不能少于6位")
    #     return value

class ProfileSerializer(ModelSerializer):
    """个人信息模型序列化器"""
    #使用AccountSerializer作为account字段的嵌套序列化器
    account = AccountSerializer(read_only=True)

    class Meta:
        model = models.Profile
        fields = ["id", "name", "account", "student_id", "wechat_id", ]
        # fields = "__all__"

class BookSerializer(ModelSerializer):
    """图书信息模型序列化器"""
    #使用AccountSerializer作为account字段的嵌套序列化器
    account = AccountSerializer(read_only=True)

    class Meta:
        model = models.Book
        # 显式指定字段，按业务重要性排序
        fields = ["id",
                  "title",
                  "original_price",
                  "current_price",
                  "img_url",
                  "place",
                  "remarks",
                  "account",
                  # "create_time",
                  # "update_time",
                  ]
        # fields = "__all__"
        # depth = 1


    # def validate(self, data):
    #     """验证现价不能高于原价"""
    #     if data.get("current_price") > data.get("original_price"):
    #         raise serializers.ValidationError("现价不能高于原价")
    #     return data

