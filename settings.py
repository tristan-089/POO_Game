from dataclasses import dataclass
from src.Armes import Arme
from src.Ennemi import Ennemi
from src.Ennemi import Boss
from src.Player import Heros

@dataclass
class Settings:
    baton = Arme("Baton", 5)
    epee = Arme("Epee", 5)

    heros = Heros("Tristan", 120, 20)
    ennemi = Ennemi("Ennemi", 65, 15)
    boss = Boss("Boss", 130, 30)