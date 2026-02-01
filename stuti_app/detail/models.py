"""
Robusr 2026.2.2
用户详情信息组件数据模型
"""
from django.db import models


class UserDetail(models.Model):
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
    # create_time = models.DateTimeField(
    #     blank=True,
    #     null=True
    # )

    class Meta:
        managed = False
        db_table = 'user_detail'
