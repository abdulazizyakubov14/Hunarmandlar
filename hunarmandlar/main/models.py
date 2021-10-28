from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField("*Title", max_length=350)
    subtitle = models.CharField("*Subtitle", max_length=350)
    image = models.ImageField("*Image", upload_to='catImage/',)
    slug = models.SlugField("*")

    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField("Tovar nomi", max_length=300)
    price = models.CharField("Narxi", max_length=150)
    img1 = models.ImageField("Rasmi 1", upload_to='product_img/')
    img2 = models.ImageField("Rasmi 2", upload_to='product_img/')
    img3 = models.ImageField("Rasmi 3", upload_to='product_img/')
    img4 = models.ImageField("Rasmi 4", upload_to='product_img/')
    CHOICES = (
        ('uzs','UZS'),
        ('usd','USD'),
        ('rub','RUB')
    )
    val = models.CharField(choices=CHOICES, max_length=50)
    category = models.ForeignKey("main.Category", related_name="product", on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name="liked_products")
    seen = models.ManyToManyField(User, related_name="seen_products")

    def __str__(self):
        return self.name

