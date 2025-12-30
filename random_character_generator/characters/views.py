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

    # Determine priority stats for class
    priority_stats = {
        'artificer': ('intelligence', 'constitution'),
        'barbarian': ('strength', 'constitution'),
        'bard': ('charisma', 'dexterity'),
        'cleric': ('wisdom', 'charisma'),
        'druid': ('wisdom', 'intelligence'),
        'fighter': ('strength', 'constitution'),
        'monk': ('dexterity', 'strength'),
        'paladin': ('strength', 'charisma'),
        'ranger': ('dexterity', 'wisdom'),
        'rogue': ('dexterity', 'intelligence'),
        'sorcerer': ('charisma', 'constitution'),
        'warlock': ('charisma', 'intelligence'),
        'wizard': ('intelligence', 'wisdom'),
    }

    primary, secondary = priority_stats.get(character_class.lower(), ('strength', 'dexterity'))

    # Generate random stats
    def generate_stat(stat_name):
        if stat_name == primary:
            return random.randint(13,18)
        elif stat_name == secondary:
            return random.randint(13,16)
        else:
            return random.randint(7,12)

    strength = generate_stat('strength')
    dexterity = generate_stat('dexterity')
    constitution = generate_stat('constitution')
    wisdom = generate_stat('wisdom')
    intelligence = generate_stat('intelligence')
    charisma = generate_stat('charisma')

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