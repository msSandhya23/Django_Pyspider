from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)
    
    def __str__(self):
        return self.topic_name
    
class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    url = models.URLField()
    email = models.EmailField(max_length=264,default='hai@gmail.com')
    
    def __str__(self):
        return self.name
    

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()
    author = models.CharField(max_length=264)
    
    def __str__(self):
        return self.author