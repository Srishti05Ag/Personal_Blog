from django.db import models


class Writings(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    writing_text = models.TextField(max_length=2000, null=True)
    likes_total = models.IntegerField(default=1)

    def __str__(self):
        return self.title
