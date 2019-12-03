from django.db import models

# Create your models here.

			
class XkomDane(models.Model):
    data = models.TextField()
    product = models.TextField()
    oldprice = models.TextField()
    newprice = models.TextField()
    dostepnosc = models.IntegerField()

    class Meta:
        db_table = 'xkom_dane'