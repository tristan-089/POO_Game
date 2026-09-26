import random, time
from settings import Settings

# Personnages
heros = Settings().heros
ennemi = Settings().ennemi
boss = Settings().boss

# Armes
epee = Settings().epee

def main():
    heros.add_arm_inventory(epee)
    print(f"Inventaire de {heros.nom} : {heros.get_heros_inventaire()}")
    time.sleep(3)
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
        print()
        time.sleep(1)

        while heros.est_vivant() and boss.est_vivant():
            if heros.est_vivant():
                if heros.vie < 15:
                    heros.regenerate_life()
                    print(f"La vie à {heros.nom} a été augmenté")
                heros.attaquer_arme(epee, boss)
                heros.get_mana()
                time.sleep(1)

                print(f"{heros.nom} : vie = {heros.vie}, mana = {heros.mana}")
                print(f"{boss.nom} : vie = {boss.vie}")
                time.sleep(1)
                print()

            if boss.est_vivant():
                boss.attaquer(heros)
                if random.randint(1, 20) == 20:
                    boss.attaque_speciale(heros)

                    print(f"{heros.nom} : vie = {heros.vie}, mana = {heros.mana}")
                    print(f"{ennemi.nom} : vie = {ennemi.vie}")
                    time.sleep(1)
                    print()

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
