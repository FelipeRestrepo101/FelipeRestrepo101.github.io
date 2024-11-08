from django.db import models


# Create your models here.
class Review(models.Model):
    Name = Rev = models.CharField(max_length=120)
    Exp = models.IntegerField()
    Rev = models.CharField(max_length=120)
    Future = models.CharField(max_length=120)
    
