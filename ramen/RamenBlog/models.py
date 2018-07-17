from django.db import models
from django.utils import timezone

class Type(models.Model):
    type = models.CharField('種類', max_length=50)

    def __str__(self):
        return self.type


class Soup(models.Model):
    type = models.CharField('スープ', max_length=50)

    def __str__(self):
        return self.type


class Prefecture(models.Model):
    prefecture = models.CharField('都道府県', max_length=10)

    def __str__(self):
        return self.prefecture


class Thickness(models.Model):
    thickness = models.CharField('麺の太さ', max_length=10)

    def __str__(self):
        return self.thickness


class Ramen(models.Model):
    name = models.CharField('店名', max_length=20)
    type = models.ForeignKey(
        Type, verbose_name = '種類', on_delete = models.PROTECT,
    )
    recommendation = models.CharField('おすすめ', max_length=20)
    soup = models.ManyToManyField(
        Soup, verbose_name = 'スープ',
    )
    location = models.ForeignKey(
        Prefecture, verbose_name = '都道府県', on_delete = models.PROTECT,
    )
    thickness = models.ForeignKey(
        Thickness, verbose_name = '麺の太さ', on_delete = models.PROTECT,
    )
    station = models.CharField('最寄り駅', max_length=20)
    wating_time = models.CharField('待ち時間', max_length=20)
    picture = models.ImageField('フォト', upload_to='img/ramen/', null=True, blank=True)
    created_at = models.DateTimeField('訪問日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.name
