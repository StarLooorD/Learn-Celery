from django.db import models


class SuperModel(models.Model):
    name = models.CharField(max_length=10)
    counter = models.IntegerField()

    def __str__(self):
        return f'Name: {self.name}, ' \
               f'Counter: {self.counter}'
