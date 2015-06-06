# -*- coding: utf-8 -*-

class Guy:
    """
    Classe modélisant un gars.

    Un gars possède une arme à munitions limitées et non rechargeable mais
    échangeable, des points de vie et des potions régénératrices. Il peut
    taper, boire un coup et changer d'arme.
    """

    # Valeurs communes
    _weapon_stats = {
        "tuba":     {"dmg": 10, "ammunitions_max": -1},  # Munitions illimitées
        "crosse":   {"dmg": 20, "ammunitions_max": 1},
        "effaceur": {"dmg": 30, "ammunitions_max": 2}
    }
    _life_max = 100
    _potions_max = 3
    _healing_points = 10

    def __init__(self, name="Anne Onime"):
        """
        Initialisation d'un gars.
        """
        self._name = name
        self._life = self._life_max
        self._potions = self._potions_max
        self._weapon = ["tuba", -1]   # Nom et munitions

    def get_stats(self):
        """
        Renvoie les statistiques du gars sous forme d'un dictionnaire
        contenant les valeurs name, life, potions et weapon. weapon est aussi
        un dictionnaire contenant les valeur name, dmg et ammunitions.
        """
        return {
            "name": self._name,
            "life": self._life,
            "potions": self._potions,
            "weapon": {
                "name": self._weapon[0],
                "dmg": self._weapon_stats[self._weapon[0]]["dmg"],
                "ammunitions": self._weapon[1]
            }
        }

    def beat(self, other_guy):
        """
        Tape un gars.

        Si self a assez de munitions, la vie d'other_guy sera réduite
        d'autant de dégats que fait l'arme de self, sinon il ne se passe rien.
        """
        if self._weapon[1] == -1 or self._weapon[1] > 0:
            other_guy._life -= self._weapon_stats[self._weapon[0]]["dmg"]
            if self._weapon[1] != -1 and self._weapon[1] != 0:
                self._weapon[1] -= 1

    def change_weapon(self, name):
        """
        Change d'arme.

        Si le nom donné en paramètre ne correspond à aucune arme,
        il ne se passe rien.
        """
        if name in self._weapon_stats.keys():
            self._weapon = [name, self._weapon_stats[name]["ammunitions_max"]]

    def drink(self):
        """
        Boit un coup et régénère la vie de 10 points si self a assez de potions.
        """
        if self._potions > 0:
            self._life += self._healing_points
            self._potions -= 1


# C'est parti, on teste
if __name__ == "__main__":
    loic = Guy("Loïc")
    hugo = Guy("Hugo")
    print(loic.get_stats())
    print(hugo.get_stats())

    i = 0
    print(i, ")-----")
    loic.beat(hugo)
    print(loic.get_stats())
    print(hugo.get_stats())

    i += 1
    print(i, ")-----")
    loic.change_weapon("ok")
    print(loic.get_stats())

    i += 1
    print(i, ")-----")
    loic.change_weapon("crosse")
    print(loic.get_stats())

    i += 1
    print(i, ")-----")
    loic.beat(hugo)
    print(loic.get_stats())
    print(hugo.get_stats())

    i += 1
    print(i, ")-----")
    loic.beat(hugo)
    print(loic.get_stats())
    print(hugo.get_stats())

    i += 1
    print(i, ")-----")
    hugo.drink()
    hugo.change_weapon("effaceur")
    print(hugo.get_stats())

    i += 1
    print(i, ")-----")
    hugo.beat(loic)
    print(loic.get_stats())
    print(hugo.get_stats())

    i += 1
    print(i, ")-----")
    hugo.beat(loic)
    print(loic.get_stats())
    print(hugo.get_stats())

    i += 1
    print(i, ")-----")
    hugo.beat(loic)
    print(loic.get_stats())
    print(hugo.get_stats())

