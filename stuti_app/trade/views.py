"""
Robusr 2026.2.2
书籍交易视图组件
"""
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView


class PendingBooksGenericAPIView(GenericAPIView):
    """基于GenericAPIView的约定交易视图方法 """



