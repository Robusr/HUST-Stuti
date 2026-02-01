"""
Robusr 2026.2.2
用户详情信息视图组件
"""
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin

from stuti_app.detail.models import UserDetail
from stuti_app.detail.serializer import UserDetailSerializer


class UserDetailGeneticAPIView(
    GenericAPIView,
    CreateModelMixin,
    RetrieveModelMixin,
):
    queryset = UserDetail.objects
    serializer_class = UserDetailSerializer

    def post(self, request):
        queryset = UserDetail.objects
        return self.create(request)

    def get(self, request, pk):
        return self.retrieve(request, pk)

