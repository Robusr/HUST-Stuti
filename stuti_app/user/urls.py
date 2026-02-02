"""
Robusr 2026.2.1
用户功能组件路由管理
"""
from django.urls import path
from .views import UserAPIView, LoginView

urlpatterns = [
    path("", UserAPIView.as_view()),
    path("login/", LoginView.as_view()),
]