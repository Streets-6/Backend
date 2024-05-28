from django.db import models
from core.models import Activity, Photo, Coordinates, Video


class Chairman(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    job_title = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField
    vk = models.URLField()
    avatar_url = models.URLField()


class Region(models.Model):
    geo_id = models.IntegerField()
    title = models.TextField()
    chairman = models.ForeignKey(
        Chairman, on_delete=models.SET_NULL, related_name="region", null=True
    )


class Infrastucture(Activity):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="infrastucture"
    )

    class Meta:
        verbose_name = "Площадка"
        verbose_name_plural = "Площадки"


class Event(Activity):
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="event"
    )

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class PhotoInfrastucture(Photo):
    event = models.ForeignKey(
        Infrastucture, on_delete=models.CASCADE, related_name="photo"
    )


class CoordinatesInfrastucture(Coordinates):
    event = models.ForeignKey(
        Infrastucture, on_delete=models.CASCADE, related_name="coordinates"
    )


class VideoInfrastucture(Video):
    event = models.ForeignKey(
        Infrastucture, on_delete=models.CASCADE, related_name="video"
    )


class PhotoEvent(Photo):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="photo"
    )


class CoordinatesEvent(Coordinates):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="coordinates"
    )


class VideoEvent(Video):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="video"
    )
