from django.db import models
from django.utils import timezone
from products.models import ProductsModel
from accounts.models import UserModel

class OrderingModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete = models.CASCADE,
                                null = False, blank = False, related_name = 'orders')
    user = models.ForeignKey(UserModel, on_delete = models.CASCADE,
                                    null = False, blank = False, related_name = 'orders')
    number = models.IntegerField(blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(default=timezone.now)
    checked_at = models.DateTimeField(null = True, blank = True)
    checked = models.BooleanField(default = False)
    size_1 = models.CharField(max_length = 264, null = True, blank = True)
    size_2 = models.CharField(max_length = 264, null = True, blank = True)
    size_3 = models.CharField(max_length = 264, null = True, blank = True)
    size_4 = models.CharField(max_length = 264, null = True, blank = True)
    size_5 = models.CharField(max_length = 264, null = True, blank = True)
    size_6 = models.CharField(max_length = 264, null = True, blank = True)
    size_7 = models.CharField(max_length = 264, null = True, blank = True)
    size_8 = models.CharField(max_length = 264, null = True, blank = True)
    size_9 = models.CharField(max_length = 264, null = True, blank = True)
    size_10 = models.CharField(max_length = 264, null = True, blank = True)
    size_11 = models.CharField(max_length = 264, null = True, blank = True)
    size_12 = models.CharField(max_length = 264, null = True, blank = True)
    size_13 = models.CharField(max_length = 264, null = True, blank = True)
    size_14 = models.CharField(max_length = 264, null = True, blank = True)

    number_1 = models.CharField(max_length = 264, null = True, blank = True)
    number_2 = models.CharField(max_length = 264, null = True, blank = True)
    number_3 = models.CharField(max_length = 264, null = True, blank = True)
    number_4 = models.CharField(max_length = 264, null = True, blank = True)
    number_5 = models.CharField(max_length = 264, null = True, blank = True)
    number_6 = models.CharField(max_length = 264, null = True, blank = True)
    number_7 = models.CharField(max_length = 264, null = True, blank = True)
    number_8 = models.CharField(max_length = 264, null = True, blank = True)
    number_9 = models.CharField(max_length = 264, null = True, blank = True)
    number_10 = models.CharField(max_length = 264, null = True, blank = True)
    number_11 = models.CharField(max_length = 264, null = True, blank = True)
    number_12 = models.CharField(max_length = 264, null = True, blank = True)
    number_13 = models.CharField(max_length = 264, null = True, blank = True)
    number_14 = models.CharField(max_length = 264, null = True, blank = True)

    def save(self, *args, **kwargs):

        if self.number_1 and self.number_1 != 0:
            self.size_1 = self.product.size_1
        if self.number_2 and self.number_2 != 0:
            self.size_2 = self.product.size_2
        if self.number_3 and self.number_3 != 0:
            self.size_3 = self.product.size_3
        if self.number_4 and self.number_4 != 0:
            self.size_4 = self.product.size_4
        if self.number_5 and self.number_5 != 0:
            self.size_5 = self.product.size_5
        if self.number_6 and self.number_6 != 0:
            self.size_6 = self.product.size_6
        if self.number_7 and self.number_7 != 0:
            self.size_7 = self.product.size_7
        if self.number_8 and self.number_8 != 0:
            self.size_8 = self.product.size_8
        if self.number_9 and self.number_9 != 0:
            self.size_9 = self.product.size_9
        if self.number_10 and self.number_10 != 0:
            self.size_10 = self.product.size_10
        if self.number_11 and self.number_11 != 0:
            self.size_11 = self.product.size_11
        if self.number_12 and self.number_12 != 0:
            self.size_12 = self.product.size_12
        if self.number_13 and self.number_13 != 0:
            self.size_13 = self.product.size_13
        if self.number_14 and self.number_14 != 0:
            self.size_14 = self.product.size_14


        super(OrderingModel, self).save(*args, **kwargs)
