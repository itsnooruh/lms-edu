from django.db import models


class Course(models.Model):
    """Course model."""

    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)
    lessons = models.ManyToManyField("Lesson", related_name="course")


class Lesson(models.Model):
    """Lesson model."""

    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)
