import random
from src.Armes import Arme

class Personnage:
    def __init__(self, nom:str, vie:int, attaque:int):
        """
        Super class for the personnages in this game
        """
        self.nom = nom
        self.attaque = attaque
        self.vie = vie

    def est_vivant(self):
        return self.vie > 0

    def get_arme(self):
        self.attaque += Arme

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} et fait {self.attaque} de dégats !")
        cible.vie -= self.attaque

    def attaquer_arme(self, arme, cible):
        cible.vie -= (arme.attaque + self.attaque)
        print(f"{self.nom} attaque {cible.nom} et fait {self.attaque} de dégats avec {arme.nom} !")

class Heros(Personnage):
    def __init__(self, nom, vie, attaque):
        super().__init__(nom, vie, attaque)
        self.mana = 0
        self.vie_max = vie
        self.inventaire = {}

    def add_arm_inventory(self, arme):
        """Ajoute une arme fournie par le programme à l'inventaire du héros."""
        self.inventaire.update({arme.nom: 1})

    def get_heros_inventaire(self):
        return self.inventaire

    def vie_max(self):
        self.vie +=1

    def get_mana(self):
        self.mana += self.attaque

    def attaque_speciale(self, cible):
        if random.randint(0, 10) == 10:
            cible.vie -= self.attaque + 10

    def ultimate(self, cible):
        cible.vie -= self.attaque + 90

    def regenerate_life(self):
        self.vie += 20
