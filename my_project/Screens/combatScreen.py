from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QGridLayout, QLabel, QStackedLayout, QSpacerItem, QTextEdit
from PySide6.QtGui import QPixmap, QTextCursor
from PySide6.QtCore import Qt, QTimer, Signal, QEventLoop
import sys
import time
import re
from ..otherClasses.playerManager import PlayerManager

class CombatScreen(QWidget):  

    switch_to_map = Signal()
    switch_to_stats = Signal()
    switch_to_inventory = Signal()
    switch_to_combat = Signal()

    def __init__(self, PM: PlayerManager):
        super().__init__()
        self.PM = PM
        self.jugador = self.PM.get_j()
        self.button_pressed = False
        
        self.combat_screen = QGridLayout()
        self.setLayout(self.combat_screen)
        
        self.setup_widgets()

    def setup_widgets(self):
        big_box1 = QWidget()
        self.box_layout1 = QGridLayout()
        self.box_layout1.setContentsMargins(0, 0, 0, 0)
        big_box1.setLayout(self.box_layout1)
        self.combat_screen.addWidget(big_box1, 0, 0)
        self.button_box = QWidget()
        self.button_layout = QGridLayout()
        self.button_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        self.button_box.setLayout(self.button_layout)
        self.combat_screen.addWidget(self.button_box)

        self.main_text_box = QTextEdit()
        self.main_text_box.setReadOnly(True)
        self.box_layout1.addWidget(self.main_text_box, 0, 0, 1, 2)

        side_bar_layout = QGridLayout()
        side_bar1 = QWidget()
        side_bar1.setLayout(side_bar_layout)
        self.combat_screen.addWidget(side_bar1, 0, 1)

        spacer1 = QSpacerItem(2, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        side_bar_layout.addItem(spacer1)
    
        button3 = QPushButton("Inventory")
        side_bar_layout.addWidget(button3)
        button3.clicked.connect(self.emit_inventory)
        
        button1 = QPushButton("Character Details")
        side_bar_layout.addWidget(button1)
        button1.clicked.connect(self.emit_stats)

        box_spacer = QSpacerItem(1, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.box_layout1.addItem(box_spacer, 1, 1)

    
        self.timer = QTimer()
        self.timer.timeout.connect(self.print_next_char)
        self.text_to_print = ""
        self.current_index = 0
        self.slotime = True

        self.generated_buttons = []

        #self.enemy_button_spawner(enemy_list)
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

    def on_button_press(self):
        self.button_pressed = True

    def wait_for_button_press(self):
        self.button_pressed = False
        loop = QEventLoop()
        while not self.button_pressed:
            QTimer.singleShot(100, loop.quit)
            loop.exec_()
   
    def start_slow_print(self, text):
        self.text_to_print = text
        self.current_index = 0
        if self.slotime:
            self.timer.start(50)  # Set timer to trigger every 50ms
        else:
            self.main_text_box.append(self.text_to_print)
            QTimer.singleShot(0, self.slow_print_done.emit)  # Emit signal immediately if not using slow print

    def print_next_char(self):
        if self.current_index < len(self.text_to_print):
            self.main_text_box.moveCursor(QTextCursor.End)
            self.main_text_box.insertPlainText(self.text_to_print[self.current_index])
            self.current_index += 1
        else:
            self.timer.stop()
            self.main_text_box.append("\n")
            #self.slow_print_done.emit()

    def option_button_spawner(self, question, button_label_list: list):
        self.destroy_generated_buttons()  
        self.start_slow_print(question)
        for button_label in button_label_list:
            button = QPushButton(button_label)
            self.button_layout.addWidget(button)
            self.generated_buttons.append(button)
            button.clicked.connect(lambda _, bl = button_label: self.main_text_box.append(f"You chose {bl}"))
            button.clicked.connect(lambda _, b1 = button_label: self.destroy_generated_buttons())
            button.clicked.connect(self.on_button_press)

    #def target_selected(self, enemy : Enemy):
    #    self.jugador.use_skill(enemy, Skills.skill1)

    def enemy_button_spawner(self, enemy_list: list):
        self.destroy_generated_buttons()  
        for enemy in enemy_list:
            button = QPushButton(enemy.name)
            self.button_layout.addWidget(button)
            self.generated_buttons.append(button)
            button.clicked.connect(lambda _, bl = enemy: self.main_text_box.append(f"You chose {bl.name}"))
            button.clicked.connect(lambda _, b1 = enemy: self.target_selected(enemy))
            button.clicked.connect(self.on_button_press)



    def clear_layout(self):
        while self.combat_screen.count():
            item = self.combat_screen.takeAt(0)
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

    

        

            
            
    