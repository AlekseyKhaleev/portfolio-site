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
    res1_head = models.TextField(default="Res1 Head Description")
    res1_span = models.TextField(default="Res1 Span Description")
    res1_lead = models.TextField(default="Res1 Lead Description")
    res2 = models.ImageField(upload_to='portfolio/images/', default="nothing")
    res2_head = models.TextField(default="Res2 Head Description")
    res2_span = models.TextField(default="Res2 Span Description")
    res2_lead = models.TextField(default="Res2 Lead Description")
    res3 = models.ImageField(upload_to='portfolio/images/', default="nothing")
    res3_head = models.TextField(default="Res3 Head Description")
    res3_span = models.TextField(default="Res3 Span Description")
    res3_lead = models.TextField(default="Res3 Lead Description")
    github = models.URLField()
    report = models.FileField(upload_to='portfolio/docs/', default="nothing")
    video = models.FileField(upload_to='portfolio/docs/', default="nothing")
    video_head = models.TextField(default="Video Head Description")
    video_span = models.TextField(default="Video Span Description")
    video_lead = models.TextField(default="Video Lead Description")

    def __str__(self):
        return self.title
