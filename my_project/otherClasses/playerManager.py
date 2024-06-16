from .playerClass import Player

class PlayerManager():
    def __init__(self):
        self.jugador = Player()

    def get_j(self) -> Player:
       return self.jugador
    
    