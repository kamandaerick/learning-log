from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
  """A topic that the user is learning about"""
  text = models.CharField(max_length=255)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """Return a string representation of the model"""
    return self.text
  
class Entry(models.Model):
  """Something a user learns about a topic"""
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  text = models.TextField()
  date_added = models.DateField(auto_now_add=True)

  class Meta:
    """Meta options for Entry model"""
    verbose_name = 'entry'
    verbose_name_plural = 'Entries'

  def __str__(self):
    """Return a string representation of themodel"""
    return f"{self.text[:50]}..." if len(self.text) > 50 else self.text