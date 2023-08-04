from django.db import models

# Create your models here.
class UserProfile(models.Model):
    nickname = models.CharField(max_length=20, unique = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=20, default=123456)

    def __str__(self):
        return self.nickname