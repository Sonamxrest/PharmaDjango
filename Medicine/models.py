from django.conf import settings
from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    disease = models.TextField()
    stock = models.IntegerField()
    price = models.FloatField()
    image = models.FileField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    date = models.DateField()
    qty = models.IntegerField(default=1)

