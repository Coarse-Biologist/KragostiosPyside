from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QGridLayout, QLabel, QStackedLayout, QSpacerItem, QTextEdit
from PySide6.QtGui import QPixmap, QTextCursor
from PySide6.QtCore import Qt, QTimer, Signal, QEventLoop
import sys, os
import time
import re 
import random
from ..GameImages import *
from ..otherClasses.mapLogic import MapLogic
from ..otherClasses.playerManager import PlayerManager

class MapScreen(QWidget):
    switch_to_map = Signal()
    switch_to_stats = Signal()
    switch_to_inventory = Signal()
    switch_to_combat = Signal()
    
    def __init__(self, PM: PlayerManager):
        super().__init__()
        self.map_logic = MapLogic(PM)
        self.PM = PM
        self.jugador = self.PM.get_j()
        self.button_pressed = False


        self.map_screen = QGridLayout()
        self.setLayout(self.map_screen)
        
        self.setup_widgets()

    def setup_widgets(self):
        big_box1 = QWidget()
        self.box_layout1 = QGridLayout()
        self.box_layout1.setContentsMargins(0, 0, 0, 0)
        big_box1.setLayout(self.box_layout1)
        self.map_screen.addWidget(big_box1, 0, 0)

        self.gridmap_image = QLabel()
        pixmap1 = QPixmap("my_project/GameImages/Natureborn_chico.jpg")
        scaled_pixmap1 = pixmap1.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.gridmap_image.setPixmap(scaled_pixmap1)
        self.gridmap_image.setGeometry(0, 0, 300, 300)
        self.box_layout1.addWidget(self.gridmap_image, 0, 0, 1, 2)

        self.main_text_box = QTextEdit()
        self.main_text_box.setReadOnly(True)
        self.box_layout1.addWidget(self.main_text_box, 1, 0, 1, 1)

        box_spacer = QSpacerItem(1, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.box_layout1.addItem(box_spacer, 3, 0)

        side_bar_layout = QVBoxLayout()
        side_bar1 = QWidget()
        side_bar1.setLayout(side_bar_layout)
        self.map_screen.addWidget(side_bar1, 0, 1)

        spacer1 = QSpacerItem(3, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        side_bar_layout.addItem(spacer1)

        self.button3 = QPushButton("Inventory")
        side_bar_layout.addWidget(self.button3)
        self.button3.clicked.connect(self.emit_inventory)
        
        self.button1 = QPushButton("Character Details")
        side_bar_layout.addWidget(self.button1)
        self.button1.clicked.connect(self.emit_stats)

        self.button_layout = QVBoxLayout()
        self.button_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.button2 = QPushButton("Choose Path")
        side_bar_layout.addWidget(self.button2)
        self.button2.clicked.connect(lambda: self.option_button_spawner(
            "Would you like to go North, South, East, or West?",
            ["North", "South", "East", "West"]))
        self.button2.clicked.connect(lambda: self.button2.hide())

        self.generated_buttons = []

    def hide_sidebar_buttons(self):
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
    
    def location_handler(self, direction: str):
        surroundings, location = self.map_logic.location_check(direction)
        self.main_text_box.append(surroundings)
        if location == "dangerous":
            button = QPushButton("Continue to Combat")
            self.button_layout.addWidget(button)
            self.hide_sidebar_buttons()
            button.clicked.connect(self.emit_combat)
        elif location == "merchant":
            button = QPushButton("See what the merchant has to offer")
            self.button_layout.addWidget(button)
            self.hide_sidebar_buttons()
            button.clicked.connect(self.emit_combat)
        elif location == "empty":
            self.destroy_generated_buttons()
            button = QPushButton("Continue along your journey")
            self.button_layout.addWidget(button)
            self.generated_buttons.append(button)
            button.clicked.connect(self.permit_path_choice)

    def emit_combat(self):
        self.switch_to_combat.emit()

    def emit_inventory(self):
        self.switch_to_inventory.emit()

    def emit_stats(self):
        self.switch_to_stats.emit()

    def reload_widgets(self):
        self.clear_layout()
        self.setup_widgets()

    def destroy_generated_buttons(self):
        for button in self.generated_buttons:
            button.hide()
        self.generated_buttons = []

    def permit_path_choice(self):
        self.destroy_generated_buttons()
        self.button2.show()

    def option_button_spawner(self, question, button_label_list: list):
        self.destroy_generated_buttons()  
        self.main_text_box.append(question)
        for button_label in button_label_list:
            button = QPushButton(button_label)
            self.button_layout.addWidget(button)
            self.generated_buttons.append(button)
            button.clicked.connect(lambda _, b1 = button_label: self.main_text_box.setText(f"You chose to journey {b1}."))
            button.clicked.connect(lambda: self.destroy_generated_buttons())
            button.clicked.connect(lambda _, b1 = button_label: self.location_handler(b1))
        self.box_layout1.addLayout(self.button_layout, 4, 0)
        
    def clear_layout(self):
        while self.map_screen.count():
            item = self.map_screen.takeAt(0)
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

    