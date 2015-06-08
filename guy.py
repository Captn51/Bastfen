# -*- coding: utf-8 -*-

class Guy:
    """Classe modélisant un gars.

    Un gars possède une arme à munitions limitées et non rechargeable mais
    échangeable, des points de vie et des potions régénératrices. Il peut
    taper, boire un coup et changer d'arme.
    """

    _WEAPONS_STATS = {
        "tuba":     {"dmg": 10, "ammunitions_max": -1}, # Munitions illimitées
        "crosse":   {"dmg": 20, "ammunitions_max": 1},
        "effaceur": {"dmg": 30, "ammunitions_max": 2}
    }
    _LIFE_MAX = 100
    _POTIONS_MAX = 3
    _HEALING_POINTS = 10

    def __init__(self, name="Anne Onime"):
        """Initialise un gars.
        """
        self._name = name
        self._life = self._LIFE_MAX
        self._potions = self._POTIONS_MAX
        self._weapon = ["tuba", -1]   # Nom et munitions actuelles

    def get_stats(self):
        """Renvoie les statistiques d'un gars.

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
                "dmg": self._WEAPONS_STATS[self._weapon[0]]["dmg"],
                "ammunitions": self._weapon[1]
            }
        }

    def beat(self, other_guy):
        """Tape un gars.

        Si self a assez de munitions, la vie d'other_guy sera réduite
        d'autant de dégats que fait l'arme de self, sinon il ne se passe rien.
        """
        if self._weapon[1] == -1 or self._weapon[1] > 0:
            other_guy._life -= self._WEAPONS_STATS[self._weapon[0]]["dmg"]
            if self._weapon[1] != -1 and self._weapon[1] != 0:
                self._weapon[1] -= 1

    def change_weapon(self, name):
        """Change d'arme.

        Si le nom donné en paramètre ne correspond à aucune arme,
        il ne se passe rien.
        """
        if name in self._WEAPONS_STATS.keys():
            self._weapon = [name, self._WEAPONS_STATS[name]["ammunitions_max"]]

    def drink(self):
        """Boit un coup.

        Cela permet de régénérer la vie de 10 points si self
        a assez de potions.
        """
        if self._potions > 0:
            self._life += self._HEALING_POINTS
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

