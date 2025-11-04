from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=100, default='Guest')
    email = models.EmailField(blank=True)
    description = models.TextField(default='I am a guest of ISMT')
    published_date = models.DateField()

    def __str__(self):
        return self.name