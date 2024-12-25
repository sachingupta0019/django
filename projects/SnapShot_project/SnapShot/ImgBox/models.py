from django.db import models

# Create your models here.
class ImgBoxDB(models.Model):
    title = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='media/uploads/')
    upload_date = models.DateField(auto_now_add=True)
