"""
Robusr 2026.2.1
书籍组件路由分配
"""
from django.urls  import path
from .views import BooksCategoryAPIView

urlpatterns = [
    path("category/<int:category_id>/<int:page>", BooksCategoryAPIView.as_view()),
]