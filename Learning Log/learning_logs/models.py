from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#this a model for the topics users will store
class Topic(models.Model):
    """A topic the user is learning about.
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text  

# Entry class inherits from Django’s base Model class, just as Topic did 
class Entry(models.Model):
    """Something specific learned about a topic.
    """
#topic, is a ForeignKey instance v. A foreign key is a 
#database term; it’s a reference to another record in the database.    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."  # Return first 50 characters of the entry
        return self.text

