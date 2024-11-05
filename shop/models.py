from django.db import models

# 管理員模型
class Admin(models.Model):
    acc_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "Admin info"

# 顧客模型
class Customer(models.Model):
    person_name = models.CharField(max_length=100, unique=True)
    acc_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "customer info"
    
# 賣家模型
class Seller(models.Model):
    person_name = models.CharField(max_length=100, unique=True)
    acc_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "seller info"

# 商品模型
class Product(models.Model):
    introduction = models.TextField()
    product_name = models.CharField(max_length=100, unique=True)
    product_quantity = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "product info"

# 交易紀錄模型 
class TradingRecord(models.Model):
    product_name = models.CharField(max_length=100)
    product_quantity = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "trading record info"

# 頁尾模型
class Footer(models.Model):
    about_us = models.TextField()
    contact_us = models.TextField()

    def __str__(self):
        return "footer info"
