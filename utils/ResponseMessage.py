"""
Robusr 2026.1.30
自定义响应工具
"""
import json

from django.http import HttpResponse


class MenuResponse():
     """
    菜单组件响应工具
     """
     @staticmethod
     def success(data):
        result = {
            "status": 1000,
            "data": data
        }
        return HttpResponse(
            json.dumps(result),
            content_type = "application/json"
        )


     @staticmethod
     def failed(data):
         return {
             "status": 1001,
             "data": data
         }

     @staticmethod
     def other(data):
         return {
             "status": 1000,
             "data": data
         }

class BooksResponse():
    """
    书籍组件响应工具
    """
    @staticmethod
    def success(data):
        result = {
            "status": 2000,
            "data": data
        }
        return HttpResponse(
            json.dumps(result),
            content_type = "application/json"
        )

    @staticmethod
    def failed(data):
        result = {
            "status": 2001,
            "data": data
        }
        return HttpResponse(
            json.dumps(result),
            content_type = "application/json"
        )

    @staticmethod
    def other(data):
        result = {
            "status": 2002,
            "data": data
        }
        return HttpResponse(
            json.dumps(result),
            content_type = "application/json"
        )