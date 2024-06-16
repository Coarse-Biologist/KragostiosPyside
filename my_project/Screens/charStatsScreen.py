from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QGridLayout, QLabel, QStackedLayout, QSpacerItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
import sys, os
from ..GameImages import *
from ..otherClasses.playerManager import PlayerManager

class CharStatsScreen(QWidget):
    switch_to_map = Signal()
    switch_to_stats = Signal()
    switch_to_inventory = Signal()
    switch_to_combat = Signal()

    def __init__(self, PM: PlayerManager):
        super().__init__()
        self.PM = PM
        self.jugador = PM.get_j()
        self.character_stats = QGridLayout()
        self.setLayout(self.character_stats)

    def setup_widgets(self):
        
        big_box3 = QWidget()
        self.box_layout3 = QGridLayout()
        self.box_layout3.setContentsMargins(0, 0, 0, 0)
        big_box3.setLayout(self.box_layout3)
        big_box3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.character_stats.addWidget(big_box3, 0, 0)

        self.side_bar_layout3 = QGridLayout()
        side_bar3 = QWidget()
        side_bar3.setLayout(self.side_bar_layout3)
        self.character_stats.addWidget(side_bar3, 0, 1)

        X = 0
        for key, value in self.jugador.player_attribute_dict().items():
            label = QLabel(f"{key} : {value}")
            self.box_layout3.addWidget(label, X, 0)
            X +=1

        inv_label6 = QLabel("Gold:")
        self.box_layout3.addWidget(inv_label6, X, 0)
        X += 1
        inv_label3 = QLabel("Equipped Items:")
        self.box_layout3.addWidget(inv_label3, X, 0)
        X += 1

        self.button4 = QPushButton("Show Map")
        self.side_bar_layout3.addWidget(self.button4, 0, 0)
        self.button4.clicked.connect(self.emit_map)
        #self.button4.clicked.connect(self.MW.map_screen.reload_widgets())
        
        spacer3 = QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.side_bar_layout3.addItem(spacer3, 1, 1)

        self.inventory_image = QLabel()
        self.inv_image_pixmap = QPixmap("my_project/GameImages/Natureborn_chico.jpg")
        scaled_pixmap = self.inv_image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.inventory_image.setPixmap(scaled_pixmap)
        self.box_layout3.addWidget(self.inventory_image)
        self.character_stats.addWidget(self.inventory_image, 1, 0, Qt.AlignRight | Qt.AlignTop)

    def emit_map(self):
        self.switch_to_map.emit()
    def emit_combat(self):
        self.switch_to_combat.emit()

    def combat_buttons(self):
        self.button4.hide()
        self.button4 = QPushButton("Return to Combat")
        self.side_bar_layout3.addWidget(self.button4, 0, 0, Qt.AlignCenter, Qt.AlignTop)
        self.button4.clicked.connect(self.emit_combat)
        #self.button4.clicked.connect(self.MW.combat_screen.reload_widgets())

    def clear_layout(self):
        while self.character_stats.count():
            item = self.character_stats.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
            else: 
                layout = item.layout()
                if layout:
                    self.clear_layout()

    def reload_widgets(self):
        self.clear_layout()
        self.setup_widgets()


