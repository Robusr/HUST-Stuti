"""
Robusr 2026.2.2
JWT加密工具
"""
import datetime
import jwt
# from django.db.models.expressions import result

from Stuti.settings import SECRET_KEY

def create_token(payload, timeout=1):
    headers = {
        'alg': 'HS256',
        'typ': 'JWT',
    }
    payload['exp'] = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=1)
    result = jwt.encode(
        headers = headers,
        payload = payload,
        key = SECRET_KEY,
        algorithm = 'HS256'
    )
    return result

def get_payload(token):
    try:
        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=['HS256']
        )
    except jwt.exceptions.DecodeError:
        print("Decode Error")
    except jwt.exceptions.ExpiredSignatureError:
        print("Expired Signature")
    except jwt.exceptions.InvalidTokenError:
        print("Invalid Token")

