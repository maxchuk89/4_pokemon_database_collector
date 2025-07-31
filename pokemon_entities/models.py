from django.db import models


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Имя на русском',
    )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Имя на английском',
    )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Имя на японском',
    )
    photo = models.ImageField(
        upload_to='pokemons',
        null=True,
        verbose_name='Изображение',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
    )
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolutions',
        verbose_name='Из кого эволюционировал',
    )

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Покемон',
    )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появился в')
    disappeared_at = models.DateTimeField(verbose_name='Исчез в')
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(verbose_name='Здоровье')
    strength = models.IntegerField(verbose_name='Сила')
    defence = models.IntegerField(verbose_name='Защита')
    stamina = models.IntegerField(verbose_name='Выносливость')

    class Meta:
        verbose_name = 'Сущность покемона'
        verbose_name_plural = 'Сущности покемонов'

    def __str__(self) -> str:
        return f'{self.pokemon.title} — {self.level} lvl'
