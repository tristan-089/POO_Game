import random, time

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

class Arme:
    def __init__(self, nom:str, attaque:int):
        self.nom = nom
        self.attaque = attaque

class Heros(Personnage):
    def __init__(self, nom, vie, attaque):
        super().__init__(nom, vie, attaque)
        self.mana = 0
        self.vie_max = vie

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

#Armes
epee = Arme("Epee", 15)
baton = Arme("Baton", 5)

# Personnages
heros = Heros("Tristan", 120, 20)
ennemi = Ennemi("Ennemi", 65, 15)
boss = Boss("Boss", 130, 30)

def main():
    print("Le combat commence...")
    print(f"{ennemi.nom} à {ennemi.vie} de vie")
    print(f"{heros.nom} à {heros.vie} de vie")
    print()
    time.sleep(3)
    while heros.est_vivant() and ennemi.est_vivant():
        if heros.est_vivant():
            if heros.vie < 15 or random.randint(1, 20) == 20:
                heros.regenerate_life()
            if random.randint(1, 3) == 3:
                heros.attaquer_arme(epee, ennemi)
                heros.get_mana()
            else:
                heros.attaquer(ennemi)
                heros.get_mana()

            print(f"{heros.nom} : vie = {heros.vie}, mana = {heros.mana}")
            print(f"{ennemi.nom} : vie = {ennemi.vie}")

            print()
            time.sleep(3)

        if ennemi.est_vivant():
            ennemi.attaquer(heros)
            if random.randint(1, 20) == 20:
                ennemi.attaque_speciale(heros)
            print(f"{heros.nom} : vie = {heros.vie}")
            print()
            time.sleep(3)

    if heros.est_vivant():
        print(f"{heros.nom} a gagné !")
        print(f"vie de {heros.nom} : {heros.vie}")
        print(f"vie de {ennemi.nom} : {ennemi.vie}")
        print("Mais ce n'est pas fini !")
        time.sleep(1)
        print(f"vie de {heros.nom} : {heros.vie}")
        time.sleep(1)
        print("Ton Arme a été boosté")
        epee.attaque += 20
        time.sleep(1)

        while heros.est_vivant() and boss.est_vivant():
            if heros.est_vivant():
                if heros.vie < 15:
                    heros.regenerate_life()
                    print(f"La vie à {heros.nom} a été augmenté")
                heros.attaquer_arme(epee, boss)
                heros.get_mana()

                print(f"{heros.nom} : vie = {heros.vie}, mana = {heros.mana}")
                print(f"{boss.nom} : vie = {boss.vie}")

            if boss.est_vivant():
                boss.attaquer(heros)
                if random.randint(1, 20) == 20:
                    boss.attaque_speciale(heros)

                    print(f"{heros.nom} : vie = {heros.vie}, mana = {heros.mana}")
                    print(f"{ennemi.nom} : vie = {ennemi.vie}")

    if heros.est_vivant():
        print(f"{heros.nom} a gagné !")
        print(f"vie de {heros.nom} : {heros.vie}")
        print(f"vie de {ennemi.nom} : {ennemi.vie}")

    else:
        print(f"{ennemi.nom} a gagné")
        print(f"vie de {heros.nom} : {heros.vie}")
        print(f"vie de {ennemi.nom} : {ennemi.vie}")

if __name__ == "__main__":
    main()