from creatureClassZ import Creature
import skillClassZ as sklz
import random
import generalFunctionsZ as genF
from printSlowlyFunctionZ import *

class Summon(Creature):
    def __init__(self, creature_name, description: str, creature_actions: list, hp: int, danger_level, controlled: bool):
        self.creature_name = creature_name
        self.description = description
        self.creature_actions = creature_actions
        self.hp = hp
        self.danger_level = danger_level
        self.controlled = controlled

    @classmethod     
    def summon_made_creature(cls, player_instance, creature_instance):
        creature = creature_instance[0]
        creature_attributes = [creature.creature_name, creature.description, creature.creature_actions, creature.hp, creature.danger_level]
        sloprint(f"You have conjured your trusty {creature.creature_name} to aid you in battle!")
        controlled = genF.option_print_iter("Shall you control the summon yourself? Or will it be autonomous?", ("control the summon", "have an automomous summon"), 2)
        if controlled == 1:
           creature_attributes.append(controlled)
           creature_attributes[5] = True
        elif controlled == 2:
            creature_attributes.append(controlled)
            creature_attributes[5] = False        
        summon = Summon(*creature_attributes)
        player_instance.has_summon.append(summon)
        return player_instance.has_summon
        



#octopus_fey = Summon("Grizzly Octopus", "a fur-covered octopus that prominently displays his single beak.", [sklz.skill1, sklz.tentacle_choke], 30, 1, True)
    
#octopus_fey = Summon("Grizzly Octopus", "a fur-covered octopus that prominently displays his single beak.", [sklz.skill1, sklz.tentacle_choke], 30, 1, True)

#octopus_fey = Summon("Grizzly Octopus", "a fur-covered octopus that prominently displays his single beak.", [sklz.skill1, sklz.tentacle_choke], 30, 1, True)
    
#option_print_iter("Will you control the summon? Will it control itself?", ("have a controlled summon", "have an independent summon"), 2)
