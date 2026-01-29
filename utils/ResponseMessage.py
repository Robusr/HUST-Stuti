"""
Robusr 2026.1.30
自定义响应工具
"""
import json

from django.http import HttpResponse


class MenuResponse():
     """
     成功状态码1000
     失败状态码1001
     其他状态码1002
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