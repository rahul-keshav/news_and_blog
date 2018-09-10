from django.db import models
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=50)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.category

class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=500,blank=True)
    post = models.TextField(blank=True)
    captions=models.TextField(blank=True)
    quote=models.CharField(max_length=200,blank=True)
    quote_by=models.CharField(max_length=100,blank=True)
    image=models.ImageField(upload_to='post_image/',blank=True)
    date= models.DateTimeField(default=now)

    def __str__(self):
        return self.title


