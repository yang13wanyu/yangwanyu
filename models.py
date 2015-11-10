from django.db import models

# Create your models here.

class author(models.Model):
    authorid=models.CharField(primary_key=True,max_length=50)
    name=models.CharField(max_length=70)
    age=models.CharField(max_length=30)
    country=models.CharField(max_length=50)
    def __unicode__(self):
        return self.authorid
    
class book(models.Model):
     isbn=models.CharField(primary_key=True,max_length=50)
     title=models.CharField(max_length=100)
     authorid=models.ForeignKey(author)
     publisher=models.CharField(max_length=70)
     publishdate=models.DateField()
     price=models.CharField(max_length=30)
     def __unicode__(self):
         return self.title


     
    

