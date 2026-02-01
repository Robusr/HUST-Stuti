"""
Robusr 2026.2.2
用户详情信息视图组件
"""
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
)

from stuti_app.detail.models import UserDetail
from stuti_app.detail.serializer import UserDetailSerializer


class UserDetailGeneticAPIView(
    GenericAPIView,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,):

    queryset = UserDetail.objects
    serializer_class = UserDetailSerializer

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

    def get(self, request):
        # 获取多个数据
        return self.list(request)


