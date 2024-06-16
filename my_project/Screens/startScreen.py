from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QWidget, QTextEdit, QGridLayout, QPushButton, QSizePolicy, QSpacerItem
from PySide6.QtCore import Qt, QTimer, Signal
import sys
from . import mapScreen as Mappy


class StartScreen(QWidget):
    switch_to_map = Signal()

    def __init__(self, PM):
        super().__init__()
        self.PM = PM
        self.jugador = self.PM.get_j()
        self.question_number = 0
        self.start_screen = QGridLayout()
        self.setLayout(self.start_screen)

        big_box1 = QWidget()
        self.box_layout1 = QGridLayout()
        self.box_layout1.setContentsMargins(0, 0, 0, 0) #creates main box container in start_screen
        big_box1.setLayout(self.box_layout1)
        self.start_screen.addWidget(big_box1)

        self.side_bar_layout = QVBoxLayout()
        side_bar1 = QWidget()
        side_bar1.setLayout(self.side_bar_layout)
        
        spacer1 = QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.side_bar_layout.addItem(spacer1)
        

        spacer2 = QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.box_layout1.addItem(spacer2, 1, 0)

        self.start_screen.addWidget(side_bar1, 0, 1)

        self.output_text_box = QTextEdit()
        
        self.output_text_box.setReadOnly(True)
        self.output_text_box.setText("Are you?.... ?... Are you the one?")
        self.box_layout1.addWidget(self.output_text_box, 0, 0)
        self.output_text_box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)  # Add the QTextEdit to the layout
        
        self.input_text_box = QLineEdit()
        self.input_text_box.setReadOnly(False)
        self.side_bar_layout.addWidget(self.input_text_box)  # Add the QLineEdit to the layout

        self.input_text_box.returnPressed.connect(self.name_selected) # output box response connected to user input box
    
        self.input_text_box.hide()

        self.generated_buttons = []

        self.continue_button_spawner()

    def continue_button_spawner(self):
        self.destroy_generated_buttons()
        button = QPushButton("Continue")
        self.side_bar_layout.addWidget(button)  
        self.generated_buttons.append(button) 
        button.clicked.connect(lambda : self.next_question(0))
        button.clicked.connect(self.destroy_generated_buttons)


    def destroy_generated_buttons(self):
        if len(self.generated_buttons) != 0:
            for button in self.generated_buttons:
                button.hide()
        self.generated_buttons = []

    def option_button_spawner(self, question, button_label_list: list):
        self.output_text_box.append(question)
        for button_label in button_label_list:
            button = QPushButton(button_label)
            self.side_bar_layout.addWidget(button)
            self.generated_buttons.append(button) 
            button.clicked.connect(lambda _, bl=button_label: self.handle_button_click(bl))
            

    def name_selected(self):
        if len(self.input_text_box.text()) != 0:
            selected_name = self.input_text_box.text()
            self.jugador.set_creature_name(selected_name)
            self.input_text_box.hide()
            self.output_text_box.setText(f"Greetings, most exaulted {selected_name}")
            self.continue_button_spawner()
            #return self.jugador
        else:
            pass
    
    def next_question(self, time):
        QTimer.singleShot(time, self.question_list)
        self.question_number += 1

    def handle_button_click(self, button_label):
        if self.question_number == 1:
            self.continue_button_spawner()
        if self.question_number == 2:
            if button_label == "Fire":
                self.output_text_box.append("You are born of fire, but can you burn a hole in the world?")
                self.jugador.classy = "FireBorn"
                self.continue_button_spawner()
            elif button_label == "Ice":
                self.output_text_box.append("You are born of ice, but can you freeze the earth and sun?")
                self.jugador.classy = "Frozen One"
                self.continue_button_spawner()
            elif button_label == "Nature":
                self.output_text_box.append("Nature's bounty embraces and empowers you.")
                self.jugador.classy = "NatureBorn"
                self.continue_button_spawner()
            elif button_label == "Ether":
                self.output_text_box.append("May heaven's thunder and lightning infuse you.")
                self.jugador.classy = "Celestial"
                self.continue_button_spawner()
        elif self.question_number == 3:
            if "Heart" in button_label:
               self.output_text_box.append("Thunderous is the beating of your heart. You recover increased hit-points per turn")
               self.jugador.hp_regen +=2
               #self.output_text_box.append(f"{self.jugador.hp_regen}")
               self.continue_button_spawner()
            elif "Spirit" in button_label:
                self.output_text_box.append("Your essence buzzes and vibrates, unstopable within you. You recover increased mana per turn")
                self.jugador.mana_regen +=2
                #self.output_text_box.append(f"{self.jugador.mana_regen}")
                self.continue_button_spawner()
        elif self.question_number == 4:
            if "Heart" in button_label:
                self.jugador.max_hp = 150
                self.output_text_box.append(f"Your vitality is far beyond ordinary mortals. You have {self.jugador.max_hp} hit-points")
                self.continue_button_spawner()
            elif "Spirit" in button_label:
                self.jugador.max_mana = 150
                self.output_text_box.append(f"The stars identfy with the energy within you. You have {self.jugador.max_mana} maximum mana")
                self.continue_button_spawner()
        elif self.question_number == 5:
            self.next_question(0)

    def emit_map(self):
        self.switch_to_map.emit()    

    def map_screen_button(self):
        self.destroy_generated_buttons()
        button = QPushButton("Show Map Screen")
        self.side_bar_layout.addWidget(button)  
        self.generated_buttons.append(button) 
        button.clicked.connect(lambda : self.emit_map)
        #button.clicked.connect(self.destroy_generated_buttons)

    def question_list(self):
        if self.question_number == 1:
            self.output_text_box.append("What are you called?")
            self.input_text_box.show()
        elif self.question_number == 2: 
            self.option_button_spawner("Of what essence is your soul composed?", ["Fire", "Ice", "Nature", "Ether"])
        elif self.question_number == 3:
            self.option_button_spawner("What fountain bubbles and flows more swiftly, your heart, or your spirit?", ["Heart (Increased health-regeneration)",
                                                                                               "Spirit (Increased magic-regeneration)"])
        elif self.question_number == 4:
            self.option_button_spawner("What well is deeper, your heart, or your spirit?", ["Heart (Increased max health)",
                                                                                               "Spirit (Increased max magic)"])
        elif self.question_number == 5:
            self.output_text_box.clear()
            self.option_button_spawner("So much power, and yet... You know nothing of it, and nothing of yourself. Awaken, find yourself and find your power.", ["Open Your Eyes"])
        elif self.question_number == 6:
            self.output_text_box.setText("You find yourself in an unfamiliar forest. No plants or trees are familiar to you, and even the soil contains combinations of colors and minerals that you had not seen or imagined. There is the chirping and buzzing of life concealed in every corner of the forest.")
            self.map_screen_button()
            self.output_text_box.setText(self.jugador.creature_name)
        
