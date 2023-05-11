from django.db import models

class Category(models.Model):
    label = models.CharField(max_length=40)
    game_category = models.ManyToManyField("Game")


# related_name="" <= similar to alias
