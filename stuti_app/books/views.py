"""
Robusr 2026.2.1
书籍数据视图组件
"""
from django.contrib.admin.templatetags.admin_list import result_list
from django.http import JsonResponse
#访问方式https://localhost:8000/books/category/1
from django.shortcuts import render
from rest_framework.views import APIView
import utils.ResponseMessage as ResponseMessage
from stuti_app.books.models import Books
from stuti_app.books.serializers import BooksSerializer


class BooksCategoryAPIView(APIView):
    """基于APIView的书籍类别视图方法"""
    def get(self, request, category_id, page):
        current_page = (page - 1) * 20
        end_data = page * 20
        category_data = Books.objects.filter(
            type_id=category_id,
        ).all()[current_page:end_data]

        result_list = []
        for data in category_data:
            result_list.append(data.__str__())

        return ResponseMessage.BooksResponse.success(result_list)

class BooksDetailAPIView(APIView):
    """基于APIView的书籍详情视图方法"""
    def get(self, request, sku_id):
        # print(sku_id)
        books_data = Books.objects.filter(
            sku_id=sku_id
        ).first()

        #序列化操作
        #序列化参数为instance
        #反序列化的参数为data
        result = BooksSerializer(instance=books_data)

        return ResponseMessage.BooksResponse.success(result.data)

