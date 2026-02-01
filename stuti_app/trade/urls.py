"""
Robusr 2026.2.2
书籍交易组件路由分配
"""

from django.urls import path, re_path
from .views import PendingBooksGenericAPIView

urlpatterns = [
    path('books/', PendingBooksGenericAPIView.as_view()),
    re_path("books/(?P<trade_no>.*)",PendingBooksGenericAPIView.as_view()),
]