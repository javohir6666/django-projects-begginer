from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class SavePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pwd = models.CharField(max_length=1000)
    hide_pwd = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
