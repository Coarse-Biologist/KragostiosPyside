from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QGridLayout, QLabel, QStackedLayout, QSpacerItem, QTextEdit
from PySide6.QtGui import QPixmap, QTextCursor
from PySide6.QtCore import Qt, QTimer, Signal, QEventLoop
import sys
import time
import re 
import random
from .playerManager import PlayerManager

class MapLogic(QWidget):
    def __init__ (self, PM: PlayerManager):
        super().__init__()
        self.PM = PM
        self.jugador = PM.get_j()

    def location_check(self, direction: str) -> str:
        if direction == "North":
            self.jugador.move_north()
        elif direction == "West":
            self.jugador.move_west
        elif direction == "East":
            self.jugador.move_east()
        elif direction == "South":
            self.jugador.move_south()
        else:
            pass
        surroundings = {"You search your surroundings but find nothing of value or interest": 1, "Your being tingles with the energy of emminent danger! Enemies are near!": 2, "You see an old man with a cart full of overflowing, old bags and chests. A Merchant!": 3}
        result_key = random.choice(list(surroundings.keys()))
        result_value = surroundings[result_key]
        if result_value == 1:
            location = "empty"
        elif result_value == 2:
            location = "dangerous"
        elif result_value == 3:
            location = "merchant"
        return result_key, location