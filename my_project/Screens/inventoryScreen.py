from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QGridLayout, QLabel, QStackedLayout, QSpacerItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
import sys, os
from ..item_module import item_storage
from ..GameImages import *

class InventoryScreen(QWidget):
    switch_to_map = Signal()
    switch_to_stats = Signal()
    switch_to_inventory = Signal()
    switch_to_combat = Signal()
    

    def __init__(self, PM):
        super().__init__()
        self.PM = PM
        self.jugador = self.PM.get_j()
        self.inventory_screen = QGridLayout()
        self.setLayout(self.inventory_screen)
        
        self.setup_widgets()

    def setup_widgets(self):

        big_box2 = QWidget()
        box_layout2 = QGridLayout()
        box_layout2.setContentsMargins(0, 0, 0, 0)
        big_box2.setLayout(box_layout2)
        big_box2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.inventory_screen.addWidget(big_box2, 0, 0)

        self.side_bar_layout2 = QGridLayout()
        side_bar2 = QWidget()
        side_bar2.setLayout(self.side_bar_layout2)
        self.inventory_screen.addWidget(side_bar2, 1, 1)
        
        inv_label1 = QLabel(f"Player name: {self.jugador.get_name()}")
        box_layout2.addWidget(inv_label1, 0, 0)
        inv_label2 = QLabel("Gold:")
        box_layout2.addWidget(inv_label2, 1, 0)
        inv_label3 = QLabel("Usable Items:")
        box_layout2.addWidget(inv_label3, 2, 0)
        
        #spacer2 = QSpacerItem(4, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        #box_layout2.addItem(spacer2)
        
        self.inventory_image = QLabel()
        self.inv_image_pixmap = QPixmap("my_project/GameImages/inventory_bag.png")
        scaled_pixmap = self.inv_image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.inventory_image.setPixmap(scaled_pixmap)
        box_layout2.addWidget(self.inventory_image, 4, 4, Qt.AlignRight | Qt.AlignBottom)

        self.button4 = QPushButton("Show Map")
        self.side_bar_layout2.addWidget(self.button4, 0, 0, Qt.AlignCenter, Qt.AlignTop)
        self.button4.clicked.connect(self.emit_map)
        #self.button4.clicked.connect(self.MW.map_screen.reload_widgets())
        
        weaponStats = QLabel(str(self.showItemStats(item_storage.ItemStorage.weapon1)))
        weaponStats.setWordWrap(True)
        box_layout2.addWidget(weaponStats)
        self.button4.clicked.connect(lambda: self.showItemStats(item_storage.ItemStorage.weapon1))

        #spacer2 = QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        #self.side_bar_layout2.addItem(spacer2)

    def emit_map(self):
        self.switch_to_map.emit()

    def emit_combat(self):
        self.switch_to_combat.emit()

    def combat_buttons(self):
        self.button4.hide()
        self.button4 = QPushButton("Return to Combat")
        self.side_bar_layout2.addWidget(self.button4, 0, 0, Qt.AlignCenter, Qt.AlignTop) 
        self.button4.clicked.connect(self.emit_combat)
        #self.button4.clicked.connect(self.MW.combat_screen.reload_widgets())
        
    def showItemStats(self, object):
        label_content = []
        if isinstance(object, item_storage.Armor):
            armorInfo = item_storage.getArmorInfo(object)
            self.main_text_box.append(armorInfo)
        elif isinstance(object, item_storage.Weapon):
            weaponInfo = item_storage.ItemStorage.getWeaponInfo(object)
            weaponInfoItems = weaponInfo.items()
            for key, value in weaponInfoItems:
                if isinstance(value, list):
                    label_content.append(str(key))
                    for item in value:
                        label_content.append(item)
                else: label_content.append(f"{key} : {value}")
        return label_content 

    def clear_layout(self):
        while self.inventory_screen.count():
            item = self.inventory_screen.takeAt(0)
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

        


