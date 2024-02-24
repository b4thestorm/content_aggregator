from django.db import models

class Shortcuts(models.Model):
   link = models.CharField(max_length=50, blank=True)
   title = models.CharField(max_length=100, blank=True)
   summary = models.CharField(max_length=250, blank=True)