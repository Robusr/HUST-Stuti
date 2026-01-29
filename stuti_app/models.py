"""
Robusr 2026.1.29
定义数据库结构
Robusr 2026.1.30
完全重构
"""
from django.db import models

#用户收藏表
class Wants(models.Model):
    """用户收藏数据表"""
    id = models.AutoField(primary_key=True, null=False, unique=True)
    sku_id  = models.CharField(null=False, max_length=255, unique=True)
    nums = models.IntegerField()
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'wants'