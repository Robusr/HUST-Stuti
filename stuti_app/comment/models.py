"""
Robusr 2026.2.2
用户评论组件数据模型
"""
from django.db import models

class Comment(models.Model):
    username = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    sku_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    content = models.TextField(
        blank=True,
        null=True,
    )
    inference_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    update_time = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
    )

    class Meta:
        managed = False,
        db_table = 'comment'
