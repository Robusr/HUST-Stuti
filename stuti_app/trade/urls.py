"""
Robusr 2026.2.2
书籍交易组件路由分配
"""

from django.urls  import path
from .views import PendingBooksGenericAPIView

urlpatterns = [
    path('books/', PendingBooksGenericAPIView.as_view()),
]