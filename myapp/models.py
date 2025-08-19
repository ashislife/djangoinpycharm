from django.db import models

# Create your models here.

# yaha se admin.py  me jayega or contact import karke model ko register karega
class Contact(models.Model):
    gmail=models.CharField(max_length=122)
    subject=models.CharField(max_length=122)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.gmail

