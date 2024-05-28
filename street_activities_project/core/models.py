from django.db import models

VIDEO_CHOISES = [
    ("V", "vertical"),
    ("H", "horizontal"),
]


class Discipline(models.Model):
    title = models.TextField()


class Activity(models.Model):
    title = models.TextField()
    vk = models.URLField()
    icon = models.URLField()
    discipline = models.ManyToManyField(
        Discipline,
        related_name="activity",
    )
    city = models.TextField()
    address = models.TextField()


class Photo(models.Model):
    url = models.URLField()


class Coordinates(models.Model):
    x = models.FloatField()
    y = models.FloatField()


class Video(models.Model):
    url = models.URLField()
    type = models.TextField(choices=VIDEO_CHOISES)
