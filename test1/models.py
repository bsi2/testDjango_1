#! coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class post(models.Model):
    author = models.ForeignKey('auth.User', max_length = 50)
    title = models.CharField(u'Заголовок', max_length = 256)
    created_data = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(u"Фото", upload_to = 'images')

    def __str__(self):
        return self.title

