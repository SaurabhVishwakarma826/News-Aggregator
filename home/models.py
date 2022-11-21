from django.db import models

class HomeNews(models.Model):
  home_title = models.CharField(max_length=200)
  home_image = models.URLField(null=True, blank=True)
  home_url = models.TextField()
  def __str__(self):
    return self.home_title

class SportsNews(models.Model):
  sports_title = models.CharField(max_length=200)
  sports_image = models.URLField(null=True, blank=True)
  sports_url = models.TextField()
  def __str__(self):
    return self.sports_title
