"""
Robusr 2026.1.30
自定义响应工具
"""
import json

from django.http import HttpResponse, JsonResponse


class MenuResponse():
     """
     菜单组件响应工具
     """
     # 菜单组件响应以1开头
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
    # 书籍组件响应以2开头
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

class WantsResponse():
    """
    书籍收藏组件响应工具
    """
    # 书籍收藏组件响应以3开头
    @staticmethod
    def success(data):
        result = {
            "status": 3000,
            "data": data
        }
        # return HttpResponse(
        #     json.dumps(result),
        #     content_type = "application/json"
        # )
        return JsonResponse(
            result,
            safe = False
        )

    @staticmethod
    def failed(data):
        result = {
            "status": 3001,
            "data": data
        }
        return JsonResponse(
            result,
            safe = False
        )

    @staticmethod
    def other(data):
        result = {
            "status": 3002,
            "data": data
        }
        return JsonResponse(
            result,
            safe = False
        )

class UserResponse():
    """
    用户组件响应工具
    """
    # y用户组件响应以4开头
    @staticmethod
    def success(data):
        result = {
            "status": 4000,
            "data": data
        }
        return JsonResponse(
            result,
            safe = False
        )

    @staticmethod
    def failed(data):
        result = {
            "status": 4001,
            "data": data
        }
        return JsonResponse(
            result,
            safe = False
        )

    @staticmethod
    def other(data):
        result = {
            "status": 4002,
            "data": data
        }
        return JsonResponse(
            result,
            safe = False
        )
