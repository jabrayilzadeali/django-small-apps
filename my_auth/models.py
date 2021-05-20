from django.db import models

# Create your models here.
class Accounts(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"index: {self.id}, username: {self.username}, email: {self.email}, password: {self.password}"