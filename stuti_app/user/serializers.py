"""
Robusr 2026.2.1
用户组件序列化工具
"""
from pyexpat.errors import messages

import datetime
from django.core.validators import validate_comma_separated_integer_list
from django.db.models.expressions import result
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from stuti_app.user.models import User
from utils.password_encode import get_md5


class UserSerializer(serializers.ModelSerializer):
    # username唯一性验证
    username = serializers.CharField(
        required=True,
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects.all(), message="EXIST!"),]
    )
    # 限制密码可读性
    password = serializers.CharField(write_only=True)

    birthday = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")
    create_date = serializers.DateTimeField(
        "%Y-%m-%d %H:%M:%S",
        required=False
    )

    # 数据验证以及数据加工
    def create(self, validated_data):
        # print("CREATE METHODS")
        # print(validated_data)
        validated_data['password'] = get_md5(validated_data['password'])
        result = User.objects.create(**validated_data)
        # create_time取当前时间
        validated_data['create_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return result
    class Meta:
        model = User
        fields = "__all__"
