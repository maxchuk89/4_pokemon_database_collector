from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity
import folium


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for entity in PokemonEntity.objects.all():
        if not entity.pokemon.image:
            continue

        add_pokemon(
            folium_map,
            entity.latitude,
            entity.longitude,
            request.build_absolute_uri(entity.pokemon.image.url),
        )

    pokemons_on_page = []

    for pokemon in Pokemon.objects.all():
        image_url = (
            request.build_absolute_uri(pokemon.image.url)
            if pokemon.image else ''
        )

        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': image_url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })
