from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField()
    

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()
    author = models.CharField(max_length=264)