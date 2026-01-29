"""
Robusr 2026.1.30
检索菜单数据模型
"""
from django.db import models

class MainMenu(models.Model):
    """书籍类别总菜单"""
    main_menu_id = models.IntegerField()
    main_menu_name = models.CharField(max_length=255)
    main_menu_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_menu'

class SubMenu(models.Model):
    """书籍类别二级菜单"""
    main_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_type = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_name = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_url = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sub_menu'
