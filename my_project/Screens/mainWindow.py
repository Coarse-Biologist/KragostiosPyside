from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QGridLayout, QLabel, QStackedLayout, QSpacerItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal, QObject
import sys, os
from . import mapScreen as Mappy
from . import inventoryScreen as Invy
from . import charStatsScreen as Statty
from . import startScreen as Starty
from . import combatScreen as Combat
from ..otherClasses.playerManager import PlayerManager

def main():
    
    app = QApplication(sys.argv)

    PM = PlayerManager()
    
    MW = MainWindow(PM)
    
    MW.setFocusPolicy(Qt.StrongFocus)
    MW.showMaximized()

    sys.exit(app.exec())

class MainWindow(QMainWindow):
    switch_to_stats = Signal()
    switch_to_inventory = Signal()
    switch_to_combat = Signal()
    switch_to_map = Signal()
    
    def __init__(self, PM):
        super().__init__()
        self.combat_active = False
        self.PM = PM
        self.jugador = self.PM.get_j()
        
        # Create a stacked layout to manage widget sets
        self.stacked_layout = QStackedLayout()
        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.stacked_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(central_widget)
        
        self.PM = PlayerManager()
        # Create screens
        self.start_screen = Starty.StartScreen(self.PM)
        self.map_screen = Mappy.MapScreen(self.PM)
        self.character_screen = Statty.CharStatsScreen(self.PM)
        self.inventory_screen = Invy.InventoryScreen(self.PM)
        self.combat_screen = Combat.CombatScreen(self.PM)
        
        
        # Add screens to stacked widget
        
        self.stacked_layout.addWidget(self.map_screen)
        self.stacked_layout.addWidget(self.character_screen)
        self.stacked_layout.addWidget(self.inventory_screen)
        self.stacked_layout.addWidget(self.combat_screen)
        self.stacked_layout.addWidget(self.start_screen)

        # Show initial widget set
        self.show_map_screen()

        self.character_screen.switch_to_combat.connect(self.show_combat_screen)
        self.character_screen.switch_to_map.connect(self.show_map_screen)
        self.character_screen.switch_to_inventory.connect(self.show_inventory_screen)
        self.inventory_screen.switch_to_combat.connect(self.show_combat_screen)
        self.inventory_screen.switch_to_map.connect(self.show_map_screen)
        self.inventory_screen.switch_to_stats.connect(self.show_character_screen) 
        self.character_screen.switch_to_inventory.connect(self.show_inventory_screen)
        self.combat_screen.switch_to_map.connect(self.show_map_screen)
        self.combat_screen.switch_to_stats.connect(self.show_character_screen)
        self.combat_screen.switch_to_inventory.connect(self.show_inventory_screen)
        self.map_screen.switch_to_stats.connect(self.show_character_screen)
        self.map_screen.switch_to_inventory.connect(self.show_inventory_screen)
        self.map_screen.switch_to_combat.connect(self.show_combat_screen)


    def show_start_screen(self):
        self.stacked_layout.setCurrentWidget(self.start_screen)

    def show_map_screen(self):
        self.map_screen.reload_widgets()
        self.stacked_layout.setCurrentWidget(self.map_screen)
  
    def show_inventory_screen(self):
        self.inventory_screen.reload_widgets()
        self.stacked_layout.setCurrentWidget(self.inventory_screen)
        if self.combat_active == True:
            self.inventory_screen.combat_buttons()

    def show_character_screen(self):
        self.character_screen.reload_widgets()
        self.stacked_layout.setCurrentWidget(self.character_screen)
        if self.combat_active == True:
            self.character_screen.combat_buttons()
        
    def show_combat_screen(self):
        self.combat_active = True
        self.combat_screen.reload_widgets()
        self.stacked_layout.setCurrentWidget(self.combat_screen)

#if __name__ == "__main__":
    #main()
    #screen_geometry = app.primaryScreen().geometry()
    #screen_width = int(screen_geometry.width())
    #screen_height = int(screen_geometry.height())
