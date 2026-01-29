"""
Robusr 2026.1.29
定义数据库结构
"""
from django.db import models

#账户表
class Account(models.Model):
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="用户名",
        help_text="用户登录的唯一标识，不可重复"
    )

    password = models.CharField(
        max_length=255,
        verbose_name="密码")
    # email = models.EmailField()
    # create_time = models.DateTimeField(
    #     auto_now_add=True,
    #     verbose_name="创建时间",
    #     null=True,
    # )  # 自动记录创建时间

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "账户"
        verbose_name_plural = "账户"  # 后台显示复数名
        #ordering = ["-create_time"]  # 按创建时间倒序

#个人信息表
class Profile(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="姓名",
        blank=True, #允许表格提交时空格
        null=True #允许为空
    )
    account = models.OneToOneField(
        # 一对一关联Account，更符合“一个账户对应一个个人信息”的逻辑
        Account,
        on_delete=models.CASCADE,
        related_name='profile', # 反向查询：account.profile 可直接获取个人信息
        verbose_name="关联账户",
        help_text="一对一关联账户，删除账户时同步删除个人信息"
    )
    student_id = models.CharField(
        max_length=20,
        verbose_name="学号",
        blank=True, #允许表格提交时空格
        null=True  #允许为空
    )
    wechat_id = models.CharField(
        max_length=50,
        verbose_name="微信号",
        blank=True, # 允许表格提交时空格
        null=True # 允许为空
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间",
        null=True,# 允许为空
    ) # 自动记录更新时间

    def __str__(self):
        return f"{self.name or '未命名'} ({self.wechat_id or '未填写'})"

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = "个人信息"
        ordering = ["name"]

#书籍信息表
class Book(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="书籍名称")
    original_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,# 保留两位小数
        default=0.00,
        verbose_name="原价",
        help_text="书籍的官方定价，保留两位小数"
    )
    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="现价",
        help_text="书籍的出售价格，保留两位小数"
    )
    img_url = models.CharField(
        max_length=500,  # 图片链接可能较长，调整长度
        null=True,
        blank=True,
        verbose_name="书籍图片链接",  # 补充verbose_name
        help_text="书籍封面/内页的URL，支持空值"
    )
    place = models.CharField(
        max_length=100,
        verbose_name="交易地点"
    )
    # wechat_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="微信号")
    remarks = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="备注",
        help_text="书籍的新旧程度等信息"
    )
    # 只关联Account，通过account.profile.wechat_id即可获取微信号，避免冗余
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="books",  # 反向查询：account.books 可获取该用户发布的所有书籍
        verbose_name="发布用户",
        help_text="外键关联发布书籍的用户，删除用户时同步删除其发布的书籍"
    )
    # create_time = models.DateTimeField(
    #     auto_now_add=True,
    #     verbose_name="发布时间",
    #     null=True,
    # )
    # update_time = models.DateTimeField(
    #     auto_now=True,
    #     verbose_name="更新时间",
    #     null=True
    # )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "书籍信息"
        verbose_name_plural = "书籍信息"
        # ordering = ["-create_time"]  # 按发布时间倒序
#
