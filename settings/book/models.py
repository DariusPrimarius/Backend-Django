from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
        
class Publisher(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
        
class Book(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    discount = models.IntegerField()
    preview = models.FileField(null=True)
    image = models.ImageField(null=True)
    last_sold = models.DateTimeField(null=True)
    subject = models.ForeignKey(Subject, on_delete = models.PROTECT, null=True)
    author = models.ForeignKey(Author, on_delete = models.PROTECT, null=True)
    publisher = models.ForeignKey(Publisher, on_delete = models.PROTECT, null=True)
    
    def __str__(self):
        return self.name
        
