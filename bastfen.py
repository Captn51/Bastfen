# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_bastfen import Ui_Bastfen
from guy import Guy

class Bastfen(QtWidgets.QMainWindow):
    """Classe implémentant la GUI du jeu.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.loic = Guy("Loïc")
        self.hugo = Guy("Hugo")

        self.ui = Ui_Bastfen()
        self.ui.setupUi(self)
        self.update_ui()

        self.ui.action_leave.triggered.connect(QtWidgets.QApplication.closeAllWindows)
        self.ui.action_leave.triggered.connect(QtWidgets.QApplication.quit)

    def update_ui(self):
        """MAJ l'interface.

        Met à jour les champs de l'interface en fonction des stats des
        deux personnages.
        """
        stats_loic = self.loic.get_stats()
        stats_hugo = self.hugo.get_stats()

        self.ui.loic_life.setText(str(stats_loic["life"]))
        self.ui.loic_potions.setText(str(stats_loic["potions"]))
        self.ui.loic_weapon_name.setText(stats_loic["weapon"]["name"])
        self.ui.loic_dmg.setText(str(stats_loic["weapon"]["dmg"]))
        ammunitions = stats_loic["weapon"]["ammunitions"]
        if ammunitions == -1:
            self.ui.loic_ammunitions.setText("-")
        else:
            self.ui.loic_ammunitions.setText(str(ammunitions))

        self.ui.hugo_life.setText(str(stats_hugo["life"]))
        self.ui.hugo_potions.setText(str(stats_hugo["potions"]))
        self.ui.hugo_weapon_name.setText(stats_hugo["weapon"]["name"])
        self.ui.hugo_dmg.setText(str(stats_hugo["weapon"]["dmg"]))
        ammunitions = stats_hugo["weapon"]["ammunitions"]
        if ammunitions == -1:
            self.ui.hugo_ammunitions.setText("-")
        else:
            self.ui.hugo_ammunitions.setText(str(ammunitions))

