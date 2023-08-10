from django.db import models

# Create your models here.
class StocksData(models.Model):
    symbol = models.CharField(primary_key=True,max_length=50)
    date = models.DateField()
    prevClose = models.FloatField()
    openPrice = models.FloatField()
    highPrice = models.FloatField()
    lowClose = models.FloatField()
    adjClose = models.FloatField()
    volume = models.IntegerField()
