"""
Robusr 2026.2.2
用户评论视图组件
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
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSetMixin

from stuti_app.comment.models import Comment
from stuti_app.comment.serializer import CommentSerializer


class CommentGenericAPIView(
    # 注意父类继承顺序
    ViewSetMixin,
    GenericAPIView,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):

    queryset = Comment.objects
    serializer_class = CommentSerializer

    def single(self, request, pk):
        print("SINGLE")
        return self.retrieve(request, pk)

    def comment_list(self, request):
        print("LIST")
        return self.list(request)

    def comment_edit(self, request, pk):
        print("UPDATE")
        return self.update(request, pk)

    def comment_save(self, request, pk=None):
        print("SAVE")
        # create不需要pk参数
        return self.create(request)

    def comment_delete(self, request, pk):
        print("DELETE")
        return self.destroy(request, pk)

