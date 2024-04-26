# models.py
from django.db import models

class registerdetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

class taskshow(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    deadline=models.DateField(max_length=100)
    subject=models.CharField(max_length=100)

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    textarea=models.CharField(max_length=1000)

class Task(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.name