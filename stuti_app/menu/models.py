"""
Robusr 2026.1.30
检索菜单数据模型
"""
import json

from django.db import models
from django.db.models.expressions import result


class MainMenu(models.Model):
    """书籍类别总菜单"""
    main_menu_id = models.IntegerField()
    main_menu_name = models.CharField(max_length=255)
    main_menu_url = models.CharField(max_length=255, blank=True, null=True)

    #自定义序列化
    def __str__(self):
        result_list = {
            "main_menu_id": self.main_menu_id,
            "main_menu_name": self.main_menu_name,
            "main_menu_url": self.main_menu_url
        }
        return json.dumps(result_list, ensure_ascii=False)


    class Meta:
        managed = True
        db_table = 'main_menu'

class SubMenu(models.Model):
    """书籍类别二级菜单"""
    main_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_type = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_name = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_url = models.CharField(max_length=255, blank=True, null=True)

    #自定义序列化
    def __str__(self):
        result_list = {
            "main_menu_id": self.main_menu_id,
            "sub_menu_id": self.sub_menu_id,
            "sub_menu_name": self.sub_menu_name,
            "sub_menu_url": self.sub_menu_url
        }
        return json.dumps(result_list, ensure_ascii=False)


    class Meta:
        managed = True
        db_table = 'sub_menu'
