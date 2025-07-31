import folium

from django.shortcuts import render, get_object_or_404

from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]


def add_pokemon(folium_map, lat, lon, image_url):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_on_page = []
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.select_related('pokemon'):
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            pokemon_entity.pokemon.image.url if pokemon_entity.pokemon.image else ''
        )

    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url if pokemon.image else '',
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    previous_evolution = pokemon.previous_evolution

    pokemon_data = {
        'pokemon_id': pokemon.id,
        'title_ru': pokemon.title,
        'img_url': pokemon.image.url if pokemon.image else '',
    }

    if previous_evolution:
        pokemon_data['previous_evolution'] = {
            'title_ru': previous_evolution.title,
            'pokemon_id': previous_evolution.id,
            'img_url': previous_evolution.image.url if previous_evolution.image else '',
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    entities = PokemonEntity.objects.filter(pokemon=pokemon)
    for entity in entities:
        add_pokemon(
            folium_map,
            entity.latitude,
            entity.longitude,
            pokemon.image.url if pokemon.image else '',
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_data,
    })
