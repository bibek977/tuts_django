from django.db import models

# Create your models here.

class Candle(models.Model):
    product = models.AutoField
    name = models.TextField(max_length=20)
    desc = models.TextField(max_length=1200)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="tuts_app/images",default="")
    # date = models.DateField()

    def __str__(self):
        return self.name
    
