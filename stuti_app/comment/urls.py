"""
Robusr 2026.2.2
用户评论组件路由管理
"""
from django.urls import re_path, path
from .views import CommentGenericAPIView

urlpatterns = [
    path('', CommentGenericAPIView.as_view({
        'get': 'comment_list',
        "post": "comment_save",
    })),
    re_path("(?P<pk>.*)/", CommentGenericAPIView.as_view({
        'get': 'single',
        "post": "comment_edit",
        "delete": "comment_delete",
    })),
]