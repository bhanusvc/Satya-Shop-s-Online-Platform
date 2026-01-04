from django.db import models

# Create your models here.
class Seller(models.Model):
    shop_name = models.CharField(max_length=50, blank=False)
    seller_name = models.CharField(max_length=40,blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    contact = models.BigIntegerField(blank=False)
    location = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.shop_name} ({self.seller_name})"
    class Meta:
        db_table = "seller_table"