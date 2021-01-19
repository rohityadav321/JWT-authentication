from django.db import models


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User, null=True)

    def __str__(self):
        return self.name
