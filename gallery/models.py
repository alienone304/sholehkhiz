from django.db import models

class GalleryModel(models.Model):
    picture = models.ImageField(default = r'gallery/default/default.jpeg',
                                 upload_to=r'gallery/')

    description = models.TextField(null = True, blank = True)
    for_product = models.BooleanField(default = False)
    for_factory = models.BooleanField(default = False)
    for_workers = models.BooleanField(default = False)
    for_sundry = models.BooleanField(default = False)
    for_excebition = models.BooleanField(default = False)

class VideoModel(models.Model):
    video = models.FileField(upload_to=r'gallery/',default = r'gallery/default/default.jpeg')
    description = models.TextField(null = True, blank = True)
