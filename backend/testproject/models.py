from email.mime import image
from django.db import models

# Create your models here.
class testData(models.Model):
    id= models.AutoField(primary_key=True, null=False, blank=False)

    views_cnt=models.IntegerField(null=True,blank=True)#조회수
    text_length=models.IntegerField(null=True,blank=True)#글자 길이
    image_cnt=models.IntegerField(null=True,blank=True,default=1)#이미지 갯수

    image=models.ImageField(upload_to="images",null=True, blank=True)#이미지
