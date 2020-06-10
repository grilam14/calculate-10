from django.db import models

class Numbers(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField()