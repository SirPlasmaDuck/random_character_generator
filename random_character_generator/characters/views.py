from django.shortcuts import render
import random
from .models import Character
from .names import CHARACTER_NAMES

def generate_random_character(request):
    # Pick a random name from the provided list
    name = random.choice(CHARACTER_NAMES)

    # Pick a random class and race
    character_class = random.choice([choice[0] for choice in Character.CLASS_CHOICES])
    character_race = random.choice([choice[0] for choice in Character.RACE_CHOICES])

    # Generate random stats
    strength = random.randint(8,15)
    dexterity = random.randint(8,15)
    constitution = random.randint(8,15)
    intelligence = random.randint(8,15)
    wisdom = random.randint(8,15)
    charisma = random.randint(8,15)

    # Create and save the character
    character = Character.objects.create(
        name = name,
        character_class = character_class,
        character_race = character_race,
        strength = strength,
        dexterity = dexterity,
        constitution = constitution,
        intelligence = intelligence,
        wisdom = wisdom,
        charisma = charisma,
    )

    return render(request, 'characters/character_detail.html', {'character': character})