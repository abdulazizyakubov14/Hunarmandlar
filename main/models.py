from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField("title", max_length=150)
    sub_title = models.CharField("sub title", max_length=450)
    slug = models.SlugField("*")
    img = models.ImageField("image", upload_to='cat_image/')

    def __str__(self):
        return self.title

    