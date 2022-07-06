from django.db import models

# Create your models here.
class Sup(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    amt = models.IntegerField()

    def __str__(self):
        return self.name
        