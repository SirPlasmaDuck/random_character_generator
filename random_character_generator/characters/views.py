from django.shortcuts import render
from django.shortcuts import redirect
import random
from .models import Character
from .names import CHARACTER_NAMES

def generate_random_character(request):
    # pick a random name from the provided list
    name = random.choice(CHARACTER_NAMES)

    # pick a random class and race
    character_class = random.choice([choice[0] for choice in Character.CLASS_CHOICES])
    character_race = random.choice([choice[0] for choice in Character.RACE_CHOICES])

    # determine stat priority reflecting the chosen class
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

    # generate the stats based on stat priority
    def generate_stat(stat_name):
        if stat_name == primary:
            return random.randint(13,18)
        elif stat_name == secondary:
            return random.randint(10,16)
        else:
            return random.randint(7,12)

    strength = generate_stat('strength')
    dexterity = generate_stat('dexterity')
    constitution = generate_stat('constitution')
    wisdom = generate_stat('wisdom')
    intelligence = generate_stat('intelligence')
    charisma = generate_stat('charisma')

    # create the character
    character = Character(
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


def save_character(request):
    if request.method == "POST":
        Character.objects.create(
            name = request.POST['name'],
            character_class = request.POST['character_class'],
            character_race = request.POST['character_race'],
            strength = request.POST['strength'],
            dexterity = request.POST['dexterity'],
            constitution = request.POST['constitution'],
            intelligence = request.POST['intelligence'],
            wisdom = request.POST['wisdom'],
            charisma = request.POST['charisma'],
        )
    return redirect('home')

def character_archive(request):
    characters = Character.objects.all()
    return render(request, 'characters/character_archive.html', {'characters': characters})