"""
Robusr 2026.1.30
书籍组件数据模型
"""
import decimal

from django.db import models
import json
from Stuti.settings import IMAGE_URL


class Books(models.Model):
    type_id = models.IntegerField(
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    sku_id = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    target_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    #原价
    origin_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    #现价
    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    image = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    seller_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    seller_id = models.IntegerField(
        blank=True,
        null=True,
    )
    #标准化单元产品ID（Standard Product Unit）
    #该二手数据标准化产品的唯一标识
    spu_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    #图书二手市场价
    market_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    publisher_id = models.IntegerField(
        blank=True,
        null=True,
    )
    find = models.IntegerField(
        blank=True,
        null=True,
    )
    create_time = models.DateTimeField(
        blank=True,
        null=True,
    )

    # 自定义序列化
    def __str__(self):
        result_list = {
            'type_id': self.type_id,
            'name': self.name,
            'sku_id': self.sku_id,
            'target_url': self.target_url,
            'origin_price': self.origin_price,
            'current_price': self.current_price,
            #书籍图片静态服务器URL拼接
            'image': IMAGE_URL + self.image,
            'seller_name': self.seller_name,
            'seller_id': self.seller_id,
            'spu_id': self.spu_id,
            'market_price': self.market_price,
            'publisher_id': self.publisher_id,
            'find': self.find,
            'create_time': self.create_time,
        }
        return json.dumps(
            result_list,
            cls=DecimalEncoder,
            ensure_ascii=False,
        )

    class Meta:
        managed = False
        db_table = 'books'

class DecimalEncoder(json.JSONEncoder):
    """数据库浮点数据类型格式转换"""
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)



