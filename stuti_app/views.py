"""
Robusr 2026.1.29
视图逻辑文件
"""
from pyexpat.errors import messages
#from .TockenAuthtication import TockenAuthtication
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse

from Stuti import settings

from .Serializer import *
from .models import *
import datetime
import jwt
import os

class LoginView(APIView):
    """登录页面视图逻辑"""
    def post(self,request):
        """返回给前端的格式"""
        ret = {
            "data":{},
            "meta":{
                "status":200,
                "message":""
            }
        }
        try:
            username = request.data['username']
            password = request.data['password']
            value = int(request.data['value'])

            if value == 1:
                user = Account.objects.filter(username=username, password=password)
                print(username, password, value, user)
                if user.count == 0:
                    ret["meta"]["status"] = 500
                    ret["meta"]["message"] = "用户不存在或密码错误"
                    return Response(ret)
                elif user and user.first().password == password:
                    dict = {
                        "exp": datetime.datetime.now() + datetime.timedelta(days=1),#过期时间
                        "iat": datetime.datetime.now(),#开始时间
                        "username": user.first().username,
                    }
                    token = jwt.encode(dict,settings.SECRET_KEY,algorithm='HS256')
                    ret["data"]["token"] = token
                    ret["data"]["username"] = user.first().username
                    ret["data"]["user_id"] = user.first().id
                    ret["meta"]["status"] = 200
                    ret["meta"]["message"] = "登录成功"
                    print(ret, type(ret))
                    return Response(ret)
                else:
                    ret["meta"]["stat us"] = 500
                    ret["meta"]["message"] = "用户不存在或密码错误"
                    return Response(ret)
        except Exception as error:
            print(error)
            ret["meta"]["status"] = 500
            ret["meta"]["message"] = "用户不存在或密码错误"
            return Response(ret)

