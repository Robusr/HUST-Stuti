"""
Robusr 2026.1.30
书籍目录菜单
"""
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from stuti_app.books.models import MainMenu, SubMenu
import utils.ResponseMessage as ResponseMessage


class BooksMainMenuView(View):
    """书籍总目录视图类"""
    def get(self, request):
        print("WantsMainView GET请求")
        main_menu = MainMenu.objects.all()
        #处理序列化数据
        result_list = []
        result_json = {}
        for main_menu_item in main_menu:
             # result_list.append(main_menu_item)
             result_list.append(main_menu_item.__str__())
        result_json['status'] = 1000
        result_json['data'] = result_list
        return HttpResponse(json.dumps(result_json), content_type="application/json")


class BooksSubMenuView(View):
    """书籍二级目录视图类"""
    def get(self, request):
        param_id = request.GET.get('main_menu_id')
        sub_menu = SubMenu.objects.filter(main_menu_id=param_id)
        result_list = []
        result_json = {}
        for sub_menu_item in sub_menu:
            # result_list.append(main_menu_item)
            result_list.append(sub_menu_item.__str__())
        # result_json['status'] = 1000
        # result_json['data'] = result_list
        return ResponseMessage.MenuResponse.success(result_list)
        # return HttpResponse(json.dumps(result_json), content_type="application/json")



