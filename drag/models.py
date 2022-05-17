from django.db import models

class Drag(models.Model):
    name = models.CharField(max_length=150)
    name_2 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        ordering = ['name']
