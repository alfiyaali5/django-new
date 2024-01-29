from django.db import models

# Create your models here.
class Bookstore(models.Model):
 def __str__(self) -> str:
    return self.bookname
 
 bookname  = models.CharField(max_length = 200)
 description = models.CharField(max_length = 500, default=None)
 price = models.FloatField(null=True, blank=True)
 available = models.BooleanField(default=False)
 image= models.ImageField(default='default.jpeg',upload_to='book_photo/')
 


  