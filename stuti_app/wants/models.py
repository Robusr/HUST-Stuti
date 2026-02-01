"""
Robusr 2026.2.1
书籍收藏组件数据模型
"""

import decimal
from django.db import models
import json

class Wants(models.Model):
    username = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sku_id = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    nums = models.IntegerField(
        null=False,
        blank=False,
    )
    is_deleted = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    create_time = models.DateTimeField(
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = 'wants'

