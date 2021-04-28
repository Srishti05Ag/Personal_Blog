from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    edit_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    def edit_date_format(self):
        return self.edit_date.strftime('%b %e, %Y')
        