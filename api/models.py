from django.db import models


class Tour(models.Model):
  title = models.CharField(max_length=100, null=False, blank=False)
  description = models.TextField(null=False, blank=False)
  image = models.ImageField()

  def __str__(self) -> str:
    return self.title


class Place(models.Model):
  title = models.CharField(max_length=100, null=False, blank=False)
  description = models.TextField(null=False, blank=False)
  likes = models.IntegerField()
  image = models.ImageField()

  def __str__(self) -> str:
    return self.title
