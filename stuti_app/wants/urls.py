"""
Robusr 2026.2.1
书籍收藏组件路由分配
"""
from django.urls  import path
from .views import WantsAPIView

urlpatterns = [
    path("", WantsAPIView.as_view()),
]