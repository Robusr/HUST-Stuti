"""
Robusr 2026.2.2
书籍交易视图组件
"""
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView

from stuti_app.trade.models import PendingBooks
from stuti_app.trade.serializers import PendingBooksSerializer


class PendingBooksGenericAPIView(GenericAPIView):
    """基于GenericAPIView的约定交易视图方法 """
    queryset = PendingBooks.objects.all()
    serializer_class = PendingBooksSerializer



