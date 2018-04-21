from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    phone = models.CharField(max_length=100, default=None)
    comments = models.TextField()

    def __str__(self):
        return self.name