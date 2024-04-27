from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title