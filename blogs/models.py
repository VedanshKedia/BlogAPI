from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Custom(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='images/error.png', blank=True, upload_to='images/')
    mail = models.EmailField(blank=True)
    number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.user.username}'


custom_object = Custom()


class BlogPost(models.Model):
    blogger = models.ForeignKey(custom_object, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.blogger}'
