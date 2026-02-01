"""
Robusr 2026.2.2
书籍交易视图组件
"""
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView

from stuti_app.trade.models import PendingBooks
from stuti_app.trade.serializers import PendingBooksSerializer


class PendingBooksGenericAPIView(GenericAPIView):
    """基于GenericAPIView的约定交易视图方法 """
    queryset = PendingBooks.objects.all()
    serializer_class = PendingBooksSerializer

    def post(self, request):
        # trade_no = request.data['trade_no']
        # self.get_queryset()
        # self.get_serializer()
        ser =  self.get_serializer(data=request.data)
        ser.is_valid()
        ser.save()
        return JsonResponse(
            "PendingBooksGenericAPIView POST",
            safe=False,
        )




