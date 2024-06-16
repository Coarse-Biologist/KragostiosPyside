from enum import Enum, auto

class SlotType(Enum):
    RIGHT_HAND = auto()
    RIGHT_FINGER =auto()
    LEFT_HAND = auto()
    LEFT_FINGER = auto()
    TWO_HAND = auto()
    HANDS = auto()
    HEAD = auto()
    CHEST = auto()
    LEGS = auto()
    FEET = auto()
    JEWELRY = auto()

    def __str__(self):
        return self.name.replace("_", " ").lower()
    
class modifiableAttributes(Enum):
    MAX_HP = auto()
    HP = auto()
    HP_REGEN = auto()
    MAX_MANA = auto()
    MANA = auto()
    MANA_REGEN = auto()
    DODGE_CHANCE = auto()
    REFLECT_CHANCE = auto()

    def __str__(self):
        return self.name.replace("_", " ").lower()
    
class effectRelevence(Enum):
    TURN_START = auto()
    TURN_END = auto
    UPON_BEING_TARGETED = auto ()
    TARGET_SELECT = auto()
    ABILITY_SELECT = auto()
    ON_DEATH = auto()
    ON_HIT = auto()
    
    def __str__(self):
        return self.name.replace("_", " ").lower()