from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Rating(models.Model):
    rating: models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    game: models.ForeignKey("Game", on_delete=models.CASCADE)
    player: models.ForeignKey("Player", on_delete=models.CASCADE)