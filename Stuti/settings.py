"""
Robusr 2026.1.30
全局基本设置
"""
# from stuti_app import books, comment, order, user, wants

"""
Robusr 2026.1.29
配置相关组件
"""
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ofe69eu75@eqy0!!#f50&zx%tc31r^tg+z+uo=d7u!k=@sb$bq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 正确的stuti_app应用配置（单独一行）
    'stuti_app.apps.StutiAppConfig',
    # corsheaders插件（单独一行，注意是纯字符串，不是配置类）
    'corsheaders',#配置跨域
    'rest_framework',#DRF组件

    # #自定义应用组件
    # "stuti_app.books",
    # "stuti_app.comment",
    # "stuti_app.order",
    # "stuti_app.wants",
    # "stuti_app.user",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',#配置跨域请求头
]

ROOT_URLCONF = 'Stuti.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Stuti.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "localhost",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "",
        "NAME": "stuti",
    }

}

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
#更换为国内时间

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

"""CORS组配置信息"""
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:8080',
#     'http://127.0.0.1:8080',
#     #如果这样写无法访问，就加上协议
#     #（http://www.localhost:8080因为不同的corsheader版本可能有不同的需求）
# )
CORS_ORIGIN_ALLOW_ALL = True
#是否允许ajax跨域请求时携带cookie，False表示不用，后面用不到cookie，所以关掉，避免cookie攻击
#请求方法
CORS_ALLOWS_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
#允许的请求头，不能用*，要写具体的请求头，不然Vue会跨域失败
CORS_ALLOWS_HEADERS = (
    "* "
)

"""媒体上传文件配置"""
#指定文件获取的url路径
MEDIA_URL = '/upimg/'

#文件上传的保存路径
MEDIA_ROOT = BASE_DIR / 'upimg'
