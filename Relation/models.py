from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13,unique=True)
    publication_date = models.DateField() 

    def __str__(self):
        return self.title