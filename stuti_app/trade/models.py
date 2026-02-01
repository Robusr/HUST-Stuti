"""
Robusr 2026.2.2
交易组件数据模型
"""
from django.db import models


class PendingBooks(models.Model):
    trade_no = models.CharField(
        max_length=255,
        db_collation='utf8mb4_general_ci',
        blank=True,
        null=True)
    sku_id = models.CharField(
        max_length=255,
        db_collation='utf8mb4_general_ci',
        blank=True,
        null=True
    )
    books_num = models.IntegerField(
        blank=True,
        null=True
    )
    create_time = models.DateTimeField(
        blank=True,
        null=True
    )
    is_delete = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'pending_books'


class Completed(models.Model):
    seller_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    seller_id = models.IntegerField(
        blank=True,
        null=True
    )
    trade_no = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    username = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    district_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    building_num = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    completed_time = models.DateTimeField(
        blank=True,
        null=True
    )
    create_time = models.DateTimeField(
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'completed'

