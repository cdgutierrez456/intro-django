from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.title
