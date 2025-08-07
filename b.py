import json
from poopybutthole import pokemonChanges

for pokemon, info in pokemonChanges.items():
    if len(info) == 6:
        new_info = [pokemon]
        new_info.extend(info)
        pokemonChanges[pokemon] = new_info

pokemonChangesNames = sorted(list(pokemonChanges.keys()))
sortedPokemonChanges = {}
for name in pokemonChangesNames:
    sortedPokemonChanges[name] = pokemonChanges[name]

with open("pokemonChanges.json", 'w') as j:
    json.dump(sortedPokemonChanges, j, indent=3)