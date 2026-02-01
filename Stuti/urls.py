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
from stuti_app import books

"""
Robusr 2026.1.29
项目总路由配置文件
"""

from django.contrib import admin
from django.urls import path, include
from stuti_app.menu.views import BooksMainMenuView, BooksSubMenuView
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('Stuti',include('Stuti.urls'), name='Stuti') #添加总路由

    #主菜单请求路由
    path("main_menu/", BooksMainMenuView.as_view()),
    path("sub_menu/", BooksSubMenuView.as_view()),
    path("books/",include("stuti_app.books.urls")),
    path("wants/",include("stuti_app.wants.urls")),
    path("user/",include("stuti_app.user.urls")),
]
