from django.db import models

class ProductsModel(models.Model):
    name = models.CharField(max_length = 264, blank = False, null = False)
    picture = models.ImageField(blank = False, null = False,default = r'products/default/default.jpeg',
                                upload_to=r'products/')
    description = models.TextField(default='',null = True, blank = True)
    is_towerdryer = models.BooleanField()
    is_radiator = models.BooleanField()
    is_waterheater = models.BooleanField()
    is_package = models.BooleanField()
    cataloge = models.FileField(blank = False, null = False, default = r'cataloges/default/default.jpeg',
                                upload_to=r'cataloges/')
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

    def save(self, *args, **kwargs):
        try:
            format = self.picture.name.lower()
            if format.endswith('.jpg') or format.endswith('.png') or format.endswith('.jpeg'):
                pass
            else:
                self.picture = None
        except:
            pass
        super(ProductsModel, self).save(*args, **kwargs)
