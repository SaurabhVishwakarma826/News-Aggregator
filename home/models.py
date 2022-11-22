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

class BusinessNews(models.Model):
  business_title = models.CharField(max_length=200)
  business_image = models.URLField(null=True, blank=True)
  business_url = models.TextField()
  def __str__(self):
      return self.business_title
  
class WorldNews(models.Model):
  world_title = models.CharField(max_length=200)
  world_image = models.URLField(null=True, blank=True)
  world_url = models.TextField()
  def __str__(self):
      return self.world_title

class PoliticsNews(models.Model):
  politics_title = models.CharField(max_length=200)
  politics_image = models.URLField(null=True, blank=True)
  politics_url = models.TextField()
  def __str__(self):
      return self.politics_title