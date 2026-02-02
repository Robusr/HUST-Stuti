"""
Robusr 2026.2.2
JWT加密工具
"""
import datetime
import jwt
from rest_framework.authentication import BaseAuthentication

# from django.db.models.expressions import result

from Stuti.settings import SECRET_KEY

def create_token(payload, timeout=1):
    headers = {
        'alg': 'HS256',
        'typ': 'JWT',
    }
    payload['exp'] = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60)
    result = jwt.encode(
        headers = headers,
        payload = payload,
        key = SECRET_KEY,
        algorithm = 'HS256'
    )
    return result

def get_payload(token):
    result = {
        "status":False,
        "data":None,
        "error":None,
    }
    try:
        # return jwt.decode(
        #     token,
        #     SECRET_KEY,
        #     algorithms=['HS256']
        # )
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        result["status"] = True
        result["data"] = payload
        result["error"] = None

    except jwt.exceptions.DecodeError:
        # print("Decode Error")
        result["error"] = "FAILED"

    except jwt.exceptions.ExpiredSignatureError:
        # print("Expired Signature")
        result["error"] = "FAILED"

    except jwt.exceptions.InvalidTokenError:
        # print("Invalid Token")
        result["error"] = "FAILED"

    return result

class JwtQueryParamAuthentication(BaseAuthentication):
    """登录组件URL验证方法"""
    def authenticate(self, request):
        # 由URL获取token
        token = request.GET.get('token')
        result_payload = get_payload(token)
        print(result_payload)
        return result_payload, token

class JwtQueryHeaderAuthentication(BaseAuthentication):
    """登录组件Header验证方法"""
    def authenticate(self, request):
        # 由Header获取token
        token = request.META.get('HTTP_TOKEN')
        print(token)
        # result_payload = get_payload(token)
        # print(result_payload)
        # return result_payload, token

