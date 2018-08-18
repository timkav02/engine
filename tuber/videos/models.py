from django.db import models
from django.core.validators import URLValidator
from taggit.managers import TaggableManager

# Create your models here.
class Video(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    embedded = models.CharField(max_length=255, validators=[URLValidator()])
    url = models.CharField(max_length=255, validators=[URLValidator()])
    rating = models.FloatField(default=0.0)
    channel = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    thumbnail = models.URLField()
    tags = TaggableManager()
    
    def __str__(self):
        return self.title

class Flipbook(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, default="")
	images = models.URLField()

	def __str__(self):
		return self.images

'''
class Tag(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, default="")
	tags = models.CharField(max_length=255)

	def __str__(self):
		return self.
'''

class Category(models.Model):
    name = models.CharField(max_length=255)
    videos_like = models.ManyToManyField(Video, related_name="categories_similar", blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Actor(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, default="")
	actors = models.CharField(max_length=255, default="", blank=True)

	def __str__(self):
		return self.actors
