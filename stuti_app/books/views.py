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


