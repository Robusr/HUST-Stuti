"""
Robusr 2026.2.2
用户详情信息视图组件
"""
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from stuti_app.detail.models import UserDetail
from stuti_app.detail.serializer import UserDetailSerializer
from utils.jwt_auth import JwtQueryParamAuthentication, JwtQueryHeaderAuthentication


class UserDetailGeneticAPIView(
    GenericAPIView,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,):

    queryset = UserDetail.objects
    serializer_class = UserDetailSerializer

    # 用户登录验证
    authentication_classes = [JwtQueryHeaderAuthentication]

    def post(self, request):
        return self.create(request)

    #lookup_field = "district_id"
    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class UserDetailListGeneticAPIView(
    GenericAPIView,
    ListModelMixin):

    queryset = UserDetail.objects
    serializer_class = UserDetailSerializer

    # 用户登录验证
    authentication_classes = [JwtQueryParamAuthentication]

    def get(self, request):
        # 获取token验证返回的第一个值
        print(request.user)
        # 获取token验证返回的第二个值
        print(request.auth)
        if not request.user.get("status"):
            return JsonResponse(request.user, safe=False)
        # 获取多个数据
        return self.list(request)


