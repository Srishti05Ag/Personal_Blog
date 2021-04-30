from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255, null=True)
    body = models.TextField(max_length=2000, null=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]
