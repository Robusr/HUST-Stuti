"""
Robusr 2026.2.2
书籍交易组件序列化工具
"""
from rest_framework import serializers

from stuti_app.trade.models import PendingBooks, Completed

class PendingBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = PendingBooks
        fields = "__all__"