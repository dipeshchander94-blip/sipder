from django.db import models

# Create your models here.
from django.db import models    
class Employee(models.Model):  
    id=models.CharField( max_length=20,primary_key=True)  
    eid = models.CharField(max_length=20)    
    ename = models.CharField(max_length=100)    
    eemail = models.EmailField()    
    econtact = models.CharField(max_length=15)    
    #class Meta:    
    #    fields = "__all__" 


from django.db import models  
class UploadedFile(models.Model):  
    title = models.CharField(max_length=100)  
    file = models.FileField(upload_to='uploads/')  
    def __str__(self):  
        return self.title  