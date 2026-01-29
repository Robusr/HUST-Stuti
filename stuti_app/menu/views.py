"""
Robusr 2026.1.30
书籍目录菜单
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class WantsMainView(View):
     def get(self, request):
         print("WantsMainView GET请求")
         return HttpResponse("WantsMainView GET请求")
