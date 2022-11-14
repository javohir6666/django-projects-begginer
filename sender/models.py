from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class EmailSender(models.Model):
    email = models.EmailField()
    theme = models.CharField(max_length=200)
    message= RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    