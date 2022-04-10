import django.utils.timezone
from django.db import models


class CardProject(models.Model):
    title = models.TextField(default="Title")
    date = models.DateField(default=django.utils.timezone.now)
    time = models.TimeField(default=django.utils.timezone.now)
    description_head = models.TextField(default="Description Head")
    description_span = models.TextField(default="Description Span")
    description_lead = models.TextField(default="Description Lead")
    logo = models.ImageField(upload_to='portfolio/images/', default="nothing")
    res1 = models.ImageField(upload_to='portfolio/images/', default="nothing")
    res1_head = models.TextField(default="Result1 Description")
    res1_span = models.TextField(default="Result1 Description")
    res1_lead = models.TextField(default="Result1 Description")
    res2 = models.ImageField(upload_to='portfolio/images/', default="nothing")
    res2_head = models.TextField(default="Result1 Description")
    res2_span = models.TextField(default="Result1 Description")
    res2_lead = models.TextField(default="Result1 Description")
    res3 = models.ImageField(upload_to='portfolio/images/', default="nothing")
    res3_head = models.TextField(default="Result1 Description")
    res3_span = models.TextField(default="Result1 Description")
    res3_lead = models.TextField(default="Result1 Description")
    url = models.URLField()
    report = models.FileField(upload_to='portfolio/docs/', default="nothing")
    video = models.FileField(upload_to='portfolio/docs/', default="nothing")

    def __str__(self):
        return self.title
