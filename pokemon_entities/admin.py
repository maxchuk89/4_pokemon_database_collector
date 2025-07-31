from django.contrib import admin

from .models import Pokemon, PokemonEntity


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'title_en', 'title_jp']
    search_fields = ['title_ru']


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ['pokemon', 'lat', 'lon', 'appeared_at', 'disappeared_at']
    list_filter = ['pokemon']
