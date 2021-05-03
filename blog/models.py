from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    poem_text = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.title
    

