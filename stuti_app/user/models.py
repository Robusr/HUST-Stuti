"""
Robusr 2026.2.1
用户信息组件数据模型
"""
from django.db import models

class User(models.Model):
    """用户信息模型"""
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    username = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    birthday = models.DateTimeField(
        null=True,
        blank=True,
    )
    mobile = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    email = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    wechat_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    student_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    password = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    create_time = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,  # 等价于MySQL的CURRENT_TIMESTAMP（创建时自动填充当前时间）
    )

    class Meta:
        managed = False
        db_table = 'user'

# class UserDetail(models.Model):
#     username = models.CharField(
#         max_length=255,
#         null=True,
#         blank=True,
#     )
#     district_id = models.CharField(
#         max_length=255,
#         null=True,
#         blank=True,
#     )
#     building_num = models.CharField(
#         max_length=255,
#         null=True,
#     )
#     create_time = models.DateTimeField(
#         null=True,
#         blank=True,
#         auto_now_add=True,
#         verbose_name="创建时间"
#     )
#
#     class Meta:
#         managed = True
#         db_table = 'user_detail'





