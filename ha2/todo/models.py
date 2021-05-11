from django.db import models


# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=160)
    deadline = models.DateField(null=True, blank=True)
    percent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.item
