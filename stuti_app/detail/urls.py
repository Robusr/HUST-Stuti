"""
Robusr 2026.2.2
用户详情信息组件路由分配
"""

from django.urls import path, re_path
from .views import UserDetailGeneticAPIView, UserDetailListGeneticAPIView

urlpatterns = [
    path('', UserDetailGeneticAPIView.as_view()),
    path("list/", UserDetailListGeneticAPIView.as_view()),
    re_path("(?P<pk>.*)/", UserDetailGeneticAPIView.as_view()),
]