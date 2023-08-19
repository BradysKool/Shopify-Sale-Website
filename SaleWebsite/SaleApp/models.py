from django.db import models

# Create your models here.
class Products(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=250)
    handle = models.CharField(max_length=100)
    msrp = models.DecimalField(max_digits=8,decimal_places=2)
    salePrice = models.DecimalField(max_digits=8,decimal_places=2)
    percentOnSale = models.DecimalField(max_digits=8,decimal_places=2,default=0.00)

    def __str__(self) -> str:
        return self.name