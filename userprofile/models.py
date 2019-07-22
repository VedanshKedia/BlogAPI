from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    username = models.OneToOneField(User, default=User, editable=False, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)
    emailid = models.EmailField(null=True, blank=True)
    number = models.CharField(max_length=10,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of MyModelName."""
    #     return reverse('model-detail-view', args=[str(self.id)])
    #
    # def __str__(self):
    #     return self.number
