import django.utils.timezone
from django.db import models


class CardProject(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=django.utils.timezone.now)
    time = models.TimeField(default=django.utils.timezone.now)
    description = models.TextField(default="Description")
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField()

    def __str__(self):
        return self.title
