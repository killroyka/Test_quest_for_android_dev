from django.db import models


# Create your models here.


class Route(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=500)
    long = models.FloatField()
    lat = models.FloatField()



class Photo(models.Model):
    route = models.ForeignKey(Route, related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField()


class RouteType(models.Model):
    routes = models.ManyToManyField(Route, related_name="types")
    title = models.CharField(max_length=40)
    title_plural = models.CharField(max_length=40)
