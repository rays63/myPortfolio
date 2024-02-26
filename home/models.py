from django.db import models

# Create your models here.
class CV(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='cv/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name