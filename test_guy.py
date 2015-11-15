# -*- coding: utf-8 -*-

import unittest
from guy import Guy


class TestGuy(unittest.TestCase):

    def test_drink(self):
        anonyme = Guy()
        self.assertEqual(anonyme.get_stats()["life"], Guy._LIFE_MAX)
        self.assertEqual(anonyme.get_stats()["potions"], Guy._POTIONS_MAX)

        # La vie ne peut dépasser la vie maximum
        anonyme.drink()
        self.assertEqual(anonyme.get_stats()["life"], Guy._LIFE_MAX)
        self.assertEqual(anonyme.get_stats()["potions"], Guy._POTIONS_MAX-1)

        anonyme._life = 0
        anonyme.drink()
        self.assertEqual(anonyme.get_stats()["life"], Guy._HEALING_POINTS)
        self.assertEqual(anonyme.get_stats()["potions"], Guy._POTIONS_MAX-2)

        # Pas de potion, pas de soin...
        anonyme._potions = 0
        anonyme.drink()
        self.assertEqual(anonyme.get_stats()["life"], Guy._HEALING_POINTS)
        self.assertEqual(anonyme.get_stats()["potions"], 0)

    def test_change_weapon(self):
        anonyme = Guy()
        self.assertEqual(anonyme.get_stats()["weapon"]["name"], "TUBA")
        self.assertEqual(anonyme.get_stats()["weapon"]["dmg"], Guy.WEAPONS_STATS["TUBA"]["dmg"])

        # Pas de nom d'arme valide, pas de chgt...
        anonyme.change_weapon("une arme bidon")
        self.assertEqual(anonyme.get_stats()["weapon"]["name"], "TUBA")
        self.assertEqual(anonyme.get_stats()["weapon"]["dmg"], Guy.WEAPONS_STATS["TUBA"]["dmg"])

        for weapon in Guy.WEAPONS_STATS.keys():
            anonyme.change_weapon(weapon)
            self.assertEqual(anonyme.get_stats()["weapon"]["name"], weapon)
            self.assertEqual(anonyme.get_stats()["weapon"]["dmg"], Guy.WEAPONS_STATS[weapon]["dmg"])

    def test_beat(self):
        loic = Guy("Loïc")
        hugo = Guy("Hugo")
        self.assertEqual(loic.get_stats()["life"], Guy._LIFE_MAX)
        self.assertEqual(hugo.get_stats()["life"], Guy._LIFE_MAX)

        # Ici, les armes sont supposées être des tubas => munitions infines
        loic.beat(hugo)
        hugo.beat(loic)
        loic.beat(hugo)
        dmg_tuba = Guy.WEAPONS_STATS["TUBA"]["dmg"]
        self.assertEqual(loic.get_stats()["life"], Guy._LIFE_MAX - dmg_tuba)
        self.assertEqual(loic.get_stats()["weapon"]["ammunitions"], Guy.UNLIMITED)
        self.assertEqual(hugo.get_stats()["life"], Guy._LIFE_MAX - 2*dmg_tuba)
        self.assertEqual(hugo.get_stats()["weapon"]["ammunitions"], Guy.UNLIMITED)

        # Pas de vie négative
        loic._life = dmg_tuba / 2
        hugo.beat(loic)
        self.assertEqual(loic.get_stats()["life"], 0)

        # Test des munitions
        loic.change_weapon("EFFACEUR")
        self.assertEqual(loic.get_stats()["weapon"]["name"], "EFFACEUR")
        self.assertEqual(Guy.WEAPONS_STATS["EFFACEUR"]["ammunitions_max"], 1)
        dmg_effaceur = Guy.WEAPONS_STATS["EFFACEUR"]["dmg"]
        hugo._life = Guy._LIFE_MAX
        loic.beat(hugo)
        self.assertEqual(hugo.get_stats()["life"], Guy._LIFE_MAX - dmg_effaceur)
        self.assertEqual(loic.get_stats()["weapon"]["ammunitions"], 0)
        loic.beat(hugo)
        self.assertEqual(hugo.get_stats()["life"], Guy._LIFE_MAX - dmg_effaceur)
        self.assertEqual(loic.get_stats()["weapon"]["ammunitions"], 0)


if __name__ == "__main__":
    unittest.main()

