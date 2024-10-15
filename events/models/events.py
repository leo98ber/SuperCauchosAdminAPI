from django.db import models


class Event(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    clients = models.ManyToManyField('clients.Client')

    def __str__(self):
        return self.name
