from django.db import models

class Character(models.Model):
    # Classes
    CLASS_CHOICES = [
        ('artificer', 'Artificer'),
        ('barbarian', 'Barbarian'),
        ('bard', 'Bard'),
        ('cleric', 'Cleric'),
        ('druid', 'Druid'),
        ('fighter', 'Fighter'),
        ('monk', 'Monk'),
        ('paladin', 'Paladin'),
        ('ranger', 'Ranger'),
        ('rogue', 'Rogue'),
        ('sorcerer', 'Sorcerer'),
        ('warlock', 'Warlock'),
        ('wizard', 'Wizard'),
    ]

    # Races
    RACE_CHOICES = [
        ('dragonborn', 'Dragonborn'),
        ('dwarf', 'Dwarf'),
        ('elf', 'Elf'),
        ('gnome', 'Gnome'),
        ('half-elf', 'Half-Elf'),
        ('half-orc', 'Half-Orc'),
        ('human', 'Human'),
        ('orc', 'Orc'),
        ('tiefling', "Tiefling")
    ]
    # Basic Information
    name = models.CharField(max_length=50)
    character_class = models.CharField(max_length=30, choices=CLASS_CHOICES)
    character_race = models.CharField(max_length=30, choices=RACE_CHOICES)

    # Stats used in 5th Edition
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    def __str__(self):
        return self.name