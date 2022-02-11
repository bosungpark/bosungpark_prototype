from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

      '''로그인 방식 선택 상자'''

      LOGIN_EMAIL='email'
      LOGIN_KAKAO='kakao'

      LOGIN_CHOICES= (
            (LOGIN_EMAIL, 'Email'),
            (LOGIN_KAKAO, 'Kakao'),
      )

      id=models.AutoField(primary_key=True)
      email=models.EmailField(max_length=100)
      login_method = models.CharField(max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL)

