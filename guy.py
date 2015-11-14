# -*- coding: utf-8 -*-

class Guy:
    """Classe modélisant un gars.

    Un gars possède une arme à munitions limitées et non rechargeable mais
    échangeable, des points de vie et des potions régénératrices. Il peut
    taper, boire un coup et changer d'arme.
    """

    UNLIMITED = -1
    WEAPONS_STATS = {
        "tuba":     {"dmg": 10, "ammunitions_max": UNLIMITED},
        "crosse":   {"dmg": 20, "ammunitions_max": 2},
        "effaceur": {"dmg": 30, "ammunitions_max": 1}
    }

    _LIFE_MAX = 100
    _POTIONS_MAX = 3
    _HEALING_POINTS = 10

    def __init__(self, name="Anne Onime"):
        """Initialise un gars.
        """
        self._name = name
        self._life = type(self)._LIFE_MAX
        self._potions = type(self)._POTIONS_MAX
        self._weapon = {
            "name": "tuba",
            "ammunitions": type(self).UNLIMITED
        }

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
                "name": self._weapon["name"],
                "dmg": type(self).WEAPONS_STATS[self._weapon["name"]]["dmg"],
                "ammunitions": self._weapon["ammunitions"]
            }
        }

    def beat(self, other_guy):
        """Tape un gars.

        Si self a assez de munitions, la vie d'other_guy sera réduite
        d'autant de dégats que fait l'arme de self, sinon il ne se passe rien.
        """
        other_guy_is_alive = (other_guy._life > 0)
        self_has_ammunitions = (self._weapon["ammunitions"] != 0)

        if other_guy_is_alive and self_has_ammunitions:
            other_guy._life -= type(self).WEAPONS_STATS[self._weapon["name"]]["dmg"]

            if other_guy._life < 0:
                other_guy._life = 0

            if self._weapon["ammunitions"] > 0:
                self._weapon["ammunitions"] -= 1

    def change_weapon(self, name):
        """Change d'arme.

        Si le nom donné en paramètre ne correspond à aucune arme,
        il ne se passe rien.
        """
        if name in type(self).WEAPONS_STATS.keys():
            self._weapon = {
                "name": name,
                "ammunitions": type(self).WEAPONS_STATS[name]["ammunitions_max"]
            }

    def drink(self):
        """Boit un coup.

        Cela permet de régénérer la vie de 10 points si self
        a assez de potions.
        """
        if self._potions > 0:
            self._life += type(self)._HEALING_POINTS
            self._potions -= 1


# TODO: tests unitaires !!

