from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator

class Game(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=280)
    designer = models.CharField(max_length=55)
    year_released  = models.IntegerField(validators=[MinValueValidator(1500), MaxLengthValidator(9999)])
    number_of_players = models.IntegerField()
    estimated_time = models.TimeField() #'00:00' 'HH:MM'
    age_recommendation = models.IntegerField()

