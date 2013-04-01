from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)

class Links(models.Model):
    user = models.ForeignKey(User)
    linkPath = models.CharField(max_length=200)
