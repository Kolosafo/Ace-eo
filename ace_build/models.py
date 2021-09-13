from django.db import models
from django.db.models.fields import FilePathField
from django.contrib.auth.models import User

# Create your models here.
class Keyword_Research(models.Model):
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.keyword
    


class Optimization (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="optimization")
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 5000)
    tags = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to="images/", blank=True, null=True)
    

    def __str__(self):
        return self.title



class ThumbnailImage (models.Model):
    image = models.ImageField(upload_to='img/%y', blank=True, null=True)
    
