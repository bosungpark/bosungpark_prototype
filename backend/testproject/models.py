from email.mime import image
from django.db import models

# Create your models here.
class testData(models.Model):
    id= models.AutoField(primary_key=True, null=False, blank=False)

    views_cnt=models.IntegerField(null=True,blank=True)
    text_length=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="images",null=True, blank=True)
