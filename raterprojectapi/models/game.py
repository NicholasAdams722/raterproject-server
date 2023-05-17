from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Game(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=280)
    designer = models.CharField(max_length=55)
    year_released  = models.IntegerField(validators=[MinValueValidator(1500), MaxValueValidator(9999)])
    number_of_players = models.IntegerField()
    estimated_time = models.DurationField() #“DD HH:MM:SS.uuuuuu”
    age_recommendation = models.IntegerField()
