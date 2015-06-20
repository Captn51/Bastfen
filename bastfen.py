# -*- coding: utf-8 -*-

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

        self._ui = Ui_Bastfen()
        self._ui.setupUi(self)
        self._update_ui()

        self._ui.action_leave.triggered.connect(QtWidgets.qApp.quit)

    def _update_ui(self):
        """MAJ l'interface.

        Met à jour les champs de l'interface en fonction des stats des
        deux personnages.
        """
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

