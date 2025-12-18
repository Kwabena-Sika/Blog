from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogTopic(models.Model):
  text = models.CharField(max_length=200)
  date_created = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.text
  
class BlogEntry(models.Model):
  title = models.ForeignKey(BlogTopic, on_delete=models.CASCADE)
  postText = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.postText[:50]}"

