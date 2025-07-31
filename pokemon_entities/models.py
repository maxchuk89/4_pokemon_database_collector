from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
