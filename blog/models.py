from django.db import models

# Create your models here.
class kasmetika(models.Model):
       name = models.CharField(max_length=100)
       bio = models.TextField()
       price = models.IntegerField()


       def __str__(self):
          return self.name


