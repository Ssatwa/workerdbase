from django.db import models
import uuid

# Create your models here.

class Worker(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    dob = models.DateField()
    education = models.CharField(max_length=200)
    id = models.UUIDField(unique=True,editable=False)
    class Meta:
        db_table = "worker"
