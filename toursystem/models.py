from django.db import models


class City(models.Model):
    title   = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Route(models.Model):
    title   = models.CharField(max_length=255)
    time    = models.CharField(max_length=255)
    other   = models.CharField(max_length=255)
    city    = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
