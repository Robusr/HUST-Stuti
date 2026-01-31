"""
Robusr 2026.2.1
书籍组件序列化器
"""
from rest_framework import serializers

from Stuti.settings import IMAGE_URL
from stuti_app.books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    """序列化处理字段"""
    # name = serializers.CharField()
    image = serializers.SerializerMethodField()
    # 时间格式序列化
    create_time = serializers.DateTimeField(
        "%Y-%m-%d %H:%M:%S",
        # read_only=True
    )

    def get_image(self, obj):
        new_image_path = IMAGE_URL + obj.image
        return new_image_path

    class Meta:
        model = Books
        fields = '__all__'


