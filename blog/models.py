
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    public_date = models.DateTimeField()
    image = models.ImageField(upload_to='post_images/')
    summary = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
