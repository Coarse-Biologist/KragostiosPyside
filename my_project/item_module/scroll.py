from .item import *

class Scroll(Item):
    def __init__(self, ability) -> None:
        self.ability = ability
    def setAbility(self, ability) -> None:
        self.ability = ability
    def use(self): #TODO -> Skill/Ability:
        return self.ability #TODO hm somehow delete item from inv after use?