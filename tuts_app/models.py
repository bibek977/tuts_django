from django.db import models

# Create your models here.

class Candle(models.Model):
    name = models.TextField(max_length=20)
    desc = models.TextField(max_length=1200)

    def __str__(self):
        return self.name
    
