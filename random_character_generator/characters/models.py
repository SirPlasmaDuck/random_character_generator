from django.db import models

class Character(models.Model):
    # Classes
    CLASS_CHOICES = [
        ('Artificer', 'Artificer'),
        ('Barbarian', 'Barbarian'),
        ('Bard', 'Bard'),
        ('Cleric', 'Cleric'),
        ('Druid', 'Druid'),
        ('Fighter', 'Fighter'),
        ('Monk', 'Monk'),
        ('Paladin', 'Paladin'),
        ('Ranger', 'Ranger'),
        ('Rogue', 'Rogue'),
        ('Sorcerer', 'Sorcerer'),
        ('Warlock', 'Warlock'),
        ('Wizard', 'Wizard'),
    ]

    # Races
    RACE_CHOICES = [
        ('Dragonborn', 'Dragonborn'),
        ('Dwarf', 'Dwarf'),
        ('Elf', 'Elf'),
        ('Gnome', 'Gnome'),
        ('Half-Elf', 'Half-Elf'),
        ('Half-Orc', 'Half-Orc'),
        ('Human', 'Human'),
        ('Orc', 'Orc'),
        ('Tiefling', "Tiefling")
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