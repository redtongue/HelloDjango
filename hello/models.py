# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

class Article(models.Model):
    title = models.CharField(u"标题",max_length=100)
    category = models.CharField(u"标签",max_length=100,blank=True)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    content = UEditorField(u"商品详情",height=300,width=1000,default=u'',blank=True,imagePath="uploads/blog/images/",toolbars="besttome",filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "商品"
        verbose_name_plural = "商品"
