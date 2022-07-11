from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Type(models.Model):
  name = models.CharField(max_length=50)
  method = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.method} {self.name}'

  def get_absolute_url(self):
    return reverse('types_detail', kwargs={'pk': self.id})

class Sup(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    amt = models.IntegerField()
    types = models.ManyToManyField(Type)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def taken_today(self):
        return self.taking_set.filter(date=date.today()).count() >= 1

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sup_id': self.id})

class Taking(models.Model):
    date = models.DateField('feeding date')
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    sup = models.ForeignKey(Sup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']