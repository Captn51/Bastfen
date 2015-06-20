# -*- coding: utf-8 -*-

from random import choice
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_bastfen import Ui_Bastfen
from guy import Guy

class Bastfen(QtWidgets.QMainWindow):
    """Classe implémentant la GUI du jeu.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self._loic = Guy("Loïc")
        self._hugo = Guy("Hugo")
        self._current_player = choice(["Loïc", "Hugo"])

        self._ui = Ui_Bastfen()
        self._ui.setupUi(self)
        self._update_ui()

        self._ui.action_leave.triggered.connect(QtWidgets.qApp.quit)
        self._ui.pb_drink.clicked.connect(self._drink)
        self._ui.pb_beat.clicked.connect(self._beat)
        self._ui.pb_change_weapon.clicked.connect(self._change_weapon)

    def _update_ui(self):
        """MAJ l'interface.

        Met à jour les champs de l'interface en fonction des stats des
        deux personnages.
        """
        #================
        # Stats des gars
        #================

        stats_loic = self._loic.get_stats()
        stats_hugo = self._hugo.get_stats()

        self._ui.loic_life.setText(str(stats_loic["life"]))
        self._ui.loic_potions.setText(str(stats_loic["potions"]))
        self._ui.loic_weapon_name.setText(stats_loic["weapon"]["name"])
        self._ui.loic_dmg.setText(str(stats_loic["weapon"]["dmg"]))
        ammunitions = stats_loic["weapon"]["ammunitions"]
        if ammunitions == Guy.UNLIMITED:
            self._ui.loic_ammunitions.setText("-")
        else:
            self._ui.loic_ammunitions.setText(str(ammunitions))

        self._ui.hugo_life.setText(str(stats_hugo["life"]))
        self._ui.hugo_potions.setText(str(stats_hugo["potions"]))
        self._ui.hugo_weapon_name.setText(stats_hugo["weapon"]["name"])
        self._ui.hugo_dmg.setText(str(stats_hugo["weapon"]["dmg"]))
        ammunitions = stats_hugo["weapon"]["ammunitions"]
        if ammunitions == Guy.UNLIMITED:
            self._ui.hugo_ammunitions.setText("-")
        else:
            self._ui.hugo_ammunitions.setText(str(ammunitions))

        #====================
        # Textes des boutons
        #====================

        player_1 = ""
        player_2 = ""
        if self._current_player == "Loïc":
            player_1 = "Loïc"
            player_2 = "Hugo"
        else:
            player_1 = "Hugo"
            player_2 = "Loïc"
        self._ui.pb_beat.setText("{} tape {}".format(player_1, player_2))
        self._ui.pb_drink.setText("{} boit un coup".format(player_1))
        self._ui.pb_change_weapon.setText("{} change d'arme".format(player_1))

    def _drink(self):
        """Un personnage boit un coup.
        """
        if self._current_player == "Loïc":
            self._loic.drink()
            self._current_player = "Hugo"
        else:
            self._hugo.drink()
            self._current_player = "Loïc"

        self._update_ui()

    def _beat(self):
        """Un gars tape l'autre.
        """
        if self._current_player == "Loïc":
            self._loic.beat(self._hugo)
            self._current_player = "Hugo"
        else:
            self._hugo.beat(self._loic)
            self._current_player = "Loïc"

        self._update_ui()

    def _change_weapon(self):
        """Un gars change d'arme.
        """
        pass

