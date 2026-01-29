"""
URL configuration for Stuti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
Robusr 2026.1.29
项目总路由配置文件
"""

from django.contrib import admin
from django.urls import path, re_path, include
from stuti_app.menu.views import WantsMainView
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('Stuti',include('Stuti.urls'), name='Stuti') #添加总路由

    #主菜单请求路由
    path("main_menu/", WantsMainView.as_view())
]
