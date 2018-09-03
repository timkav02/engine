from django.db import models
from django.core.validators import URLValidator
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class TaggedVideo(TaggedItemBase):
    content_object = models.ForeignKey('Video', on_delete=models.CASCADE)
	
# Create your models here.
class Video(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    embedded = models.CharField(max_length=255, validators=[URLValidator()])
    url = models.CharField(max_length=255, validators=[URLValidator()])
    rating = models.FloatField(default=0.0)
    channel = models.CharField(max_length=128, db_index=True)
    title = models.CharField(max_length=128, db_index=True)
    views = models.IntegerField(default=0)
    thumbnail = models.URLField()
    tags = TaggableManager(through=TaggedVideo)
    
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
'''
class Category(models.Model):
    name = models.CharField(max_length=255)
    videos_like = models.ManyToManyField(Video, related_name="video_categories", blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
'''
class Actor(models.Model):
	video = models.ForeignKey(Video, related_name="video_actors", on_delete=models.CASCADE, default="")
	actors = models.CharField(max_length=255, default="", blank=True)

	def __str__(self):
		return self.actors
