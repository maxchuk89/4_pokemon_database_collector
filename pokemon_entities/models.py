from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('Название на русском', max_length=200)
    title_en = models.CharField('Название на английском', max_length=200, blank=True)
    title_jp = models.CharField('Название на японском', max_length=200, blank=True)
    image = models.ImageField('Изображение', upload_to='pokemons', blank=True)
    description = models.TextField('Описание', blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Предыдущая эволюция',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='next_evolutions'
    )

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Покемон',
        on_delete=models.CASCADE,
        related_name='entities'
    )
    lat = models.FloatField('Широта', blank=True, null=True)
    lon = models.FloatField('Долгота', blank=True, null=True)
    appeared_at = models.DateTimeField('Появляется в', blank=True, null=True)
    disappeared_at = models.DateTimeField('Исчезает в', blank=True, null=True)
    level = models.IntegerField('Уровень', blank=True, null=True)
    health = models.IntegerField('Здоровье', blank=True, null=True)
    strength = models.IntegerField('Сила', blank=True, null=True)
    defence = models.IntegerField('Защита', blank=True, null=True)
    stamina = models.IntegerField('Выносливость', blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon} — уровень {self.level or "?"}'

    class Meta:
        verbose_name = 'Появление покемона'
        verbose_name_plural = 'Появления покемонов'
