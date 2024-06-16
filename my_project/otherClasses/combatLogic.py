from .playerClass import Player
from .enemyClass import Enemy
from .skillClass import Skills

class CombatLogic():
    def __init__(self, combatants : list = [], turn_counter : int = 10, status_dicts : dict =  {}):
        self.combatants = combatants
        self.turn_counter = turn_counter
        self.status_dicts = status_dicts

    @classmethod
    def create_combat_instance(cls, normal_enemies : int = 1, unique_enemies : int = 0):
        enemies_list = Enemy.make_creature_obj(normal_enemies, unique_enemies)
        enemies_list.append("squiddle")


        




    #self.combats_completed = 0
    #   
    #@classmethod  
    #def combat_completed(self):
    #    self.combats_completed += 1 
#
    #@classmethod  
    #def get_combat_completed(self):
    #    return self.combat_completed
    #