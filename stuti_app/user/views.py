"""
Robusr 2026.2.1
用户功能视图组件
"""
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from stuti_app.user.models import User
from stuti_app.user.serializers import UserSerializer
from utils import ResponseMessage
from utils.password_encode import get_md5


class UserAPIView(APIView):
    """基于APIView的用户视图方法"""
    # # 实现注册功能
    # def post(self, request):
    #     # 密码加密
    #     request.data['password'] = get_md5(request.data['password'])
    #
    #     # 数据反序列化
    #     user_data_serializer = UserSerializer(data=request.data)
    #     user_data_serializer.is_valid(raise_exception=True)
    #     user_data = User.objects.create(**user_data_serializer.validated_data)
    #
    #     # 数据序列化，返回给前端
    #     user_ser = UserSerializer(instance=user_data)
    #     return JsonResponse(user_ser.data)

    def post(self, request):
        # 数据反序列化
        user_data_serializer = UserSerializer(data=request.data)
        user_data_serializer.is_valid(raise_exception=True)
        user_data = user_data_serializer.save()

        # 数据序列化
        user_ser = UserSerializer(instance=user_data)
        # return JsonResponse(user_ser.data)
        return ResponseMessage.UserResponse.success(user_ser.data)

    def get(self, request):
        username = request.GET.get('username')
        try:
            user_data = User.objects.get(username=username)

            # 数据序列化
            user_ser = UserSerializer(user_data)
            return ResponseMessage.UserResponse.success(user_ser.data)
        except Exception as e:
            print(e)
            return ResponseMessage.UserResponse.failed("FAILED!")
