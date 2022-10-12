from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class new_place(models.Model):
    imag=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=250)
    descript=models.TextField()

    def __str__(self):
        return self.name
