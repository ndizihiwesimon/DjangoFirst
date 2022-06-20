from django.db import models

# Create your models here.

class Trainee(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.full_name