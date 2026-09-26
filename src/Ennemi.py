import random
from src.Player import Personnage

class Ennemi(Personnage):
    def __init__(self, nom, vie, attaque):
        super().__init__(nom, vie, attaque)

    def attaque_speciale(self, cible):
        if random.randint(0, 10) == 10:
            cible.vie -= self.attaque + 12


class Boss(Personnage):
    def __init__(self, nom, vie, attaque):
        super().__init__(nom, vie, attaque)

    def attaque_speciale(self, cible):
        if random.randint(0, 20) == 10:
            cible.vie -= self.attaque + 50