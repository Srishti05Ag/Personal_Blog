from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    url = models.TextField()
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def summary(self):
        return self.summary[:50]

    def pub_date_format(self):
        return self.pub_date.strftime('%b %e, %Y')
    

 
