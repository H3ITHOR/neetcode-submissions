class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name: str = name
        self.power: str = power
        self.health: int = health


# TODO: Create Superhero instances

s1: SuperHero = SuperHero("Batman", "Intelligence", 100)
s2: SuperHero = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(f"{s1.name}\n{s1.power}\n{s1.health}")
print(f"{s2.name}\n{s2.power}\n{s2.health}")
