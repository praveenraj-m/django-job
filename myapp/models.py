from django.db import models

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=False)
    salary = models.IntegerField()
    location = models.CharField(max_length=200)
    expiry = models.DateField(auto_now_add=False)    
    def __str__(self) :
        return f"{self.title} with salary {self.salary}"

    