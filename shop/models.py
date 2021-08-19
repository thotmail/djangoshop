from django.db import models
from django.contrib.auth.models import User

from djmoney.models.fields import MoneyField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True, default = None)

    def __str__(self):
        return self.name

    def get_parents(self):
        l = [self]
        while l[-1].parent is not None:
            l.append(l[-1].parent)
        return l[::-1]


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = MoneyField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.pk)+" : "+str(self.user)+' : '+str(self.date)

class OrderedProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = MoneyField(max_digits=10, decimal_places=2, null=True)
    class Meta:
        unique_together = (("order", "product"),)
