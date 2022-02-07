from django.urls import path
from . import views

app_name='testproject'

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('<int:id>', views.detail, name='detail'),
]