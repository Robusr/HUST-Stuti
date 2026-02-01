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
        verbose_name="姓名"
    )
    username = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="用户名"
    )
    birthday = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="出生日期"
    )
    mobile = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="手机号"
    )
    email = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="邮箱"
    )
    wechat_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="微信ID"
    )
    student_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="学号"
    )
    password = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="密码"
    )
    create_time = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,  # 等价于MySQL的CURRENT_TIMESTAMP（创建时自动填充当前时间）
        verbose_name="创建时间"
    )

    class Meta:
        managed = False
        db_table = 'user'

class UserDetail(models.Model):
    username = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    district_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    building_num = models.CharField(
        max_length=255,
        null=True,
    )
    create_time = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
        verbose_name="创建时间"
    )

    class Meta:
        managed = False
        db_table = 'user_detail'

