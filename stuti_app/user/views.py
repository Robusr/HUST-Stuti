"""
Robusr 2026.2.1
用户功能视图组件
"""
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from stuti_app.user.models import User
from stuti_app.user.serializers import UserSerializer
from utils import ResponseMessage
from utils.jwt_auth import create_token
from utils.password_encode import get_md5


class UserAPIView(APIView):

    """基于APIView的用户视图方法"""
    # @todo 重构user组件view.UserAPIView方法APIView继承类至GenericAPIView继承类

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

class LoginView(GenericAPIView):
    """用户登录视图方法"""
    # @todo 重构user组件view.LoginView组件APIView继承类至GenericAPIView继承类
    # GenericAPIView继承类需指定序列化器serializer_class
    serializer_class = UserSerializer
    def post(self, request):
        # # 显式指定仅支持POST和OPTIONS（OPTIONS是跨域预检请求，需保留）
        # http_method_names = ['post', 'options']
        return_data = {}
        request_data = request.data
        username = request.data.get('username')
        user_data = User.objects.get(username=username)

        if not user_data:
            return ResponseMessage.UserResponse.other("FAILED!")
        else:
            user_ser = UserSerializer(
                instance=user_data,
                many=False
            )
            # 用户输入密码
            user_password = request_data.get('password')
            md5_user_password = get_md5(user_password)
            # print(md5_user_password)
            # 数据库的密码
            db_user_password = user_ser.data.get('password')
            # print(db_user_password)

            if md5_user_password != db_user_password:
                return ResponseMessage.UserResponse.other("FAILED!")
            else:
                token_info = {
                    'username': username,
                }
                token_data = create_token(token_info)
                return_data['token'] = token_data
                return_data['name'] = user_ser.data.get("name")
                return ResponseMessage.UserResponse.success(return_data)
