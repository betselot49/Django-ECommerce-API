import os
from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible


@deconstructible
class GenerateImagePath(object):
     
     def __init__(self):
         pass
     
     def __call__(self, instance, filename: str) -> str:
        ext = filename.split('.')[-1]
        path = f'accounts/{instance.user.id}/images/'
        name = f'profile_image.{ext}'   
        return os.path.join(path, name) 
     

user_profile_image = GenerateImagePath()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_profile_image, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user.username}\'s Profile'