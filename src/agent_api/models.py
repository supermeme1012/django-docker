import uuid
from django.db import models

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    birthday = models.DateField(default='1970-01-01')
    occupation = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    name = models.ForeignKey(Person,on_delete=callable)
    distance = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(max_length=100,default='1970:01:01 00:00:00')
# Create your models here.
