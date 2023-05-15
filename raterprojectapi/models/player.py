from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    # name: models.CharField(max_length=55)
    age: models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
