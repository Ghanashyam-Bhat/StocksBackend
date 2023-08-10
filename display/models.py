from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    prefer = models.CharField(max_length=10,default="weekly")

class Symbol(models.Model):
    id = models.CharField(primary_key=True,max_length=50)

class userSymbols(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    symbol = models.ForeignKey(Symbol,on_delete=models.CASCADE)
    class Meta:
        unique_together = (('user','symbol'),)
