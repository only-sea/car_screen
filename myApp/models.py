from django.db import models

# Create your models here.
class carInfo(models.Model):
    id = models.AutoField('id',primary_key=True)
    brand = models.CharField('品牌',max_length=225,default='')
    carName = models.CharField('车名', max_length=225, default='')
    carImg = models.CharField('图片链接', max_length=225, default='')
    saleVolume = models.CharField('销量', max_length=225, default='')
    price = models.CharField('价格', max_length=225, default='')
    manufacturer = models.CharField('厂商', max_length=225, default='')
    rank = models.CharField('排名', max_length=225, default='')
    carModel = models.CharField('车型', max_length=225, default='')
    energyType = models.CharField('能源类型', max_length=225, default='')
    marketTime = models.CharField('上市时间', max_length=225, default='')
    insure = models.CharField('保修时间', max_length=225, default='')
    createTime = models.DateField('创建时间', auto_now_add=True)
    class Meta:
        db_table = 'carInfo'

class User(models.Model):
    id = models.AutoField('id',primary_key=True)
    username = models.CharField('用户名',max_length=225,default='')
    password = models.CharField('密码',max_length=225,default='')
    createTime = models.DateField('创建时间', auto_now_add=True)
    class Meta:
        db_table = 'User'

