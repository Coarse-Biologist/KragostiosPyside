from .item import Item, ItemRarity
from .item_equipable import *
from enum import Enum, auto

class ArmorType(Enum):
    IRON = auto()
    EFLISH = auto()
    LEATHER = auto()
    
    def __str__(self):
        return self.name.replace("_", " ").lower()

class Armor(Item, Equipable):
    def __init__(self, name = "", itemType = None, value = 0, rarity = ItemRarity.COMMON, armorValue = 1, armorType = None, slot : myEnums.SlotType = None) -> None:
        super(Item, self).__init__()#name, ItemType.ARMOR , value, rarity)
        super(Equipable, self).__init__()

        self.name = name
        self.itemType = itemType
        self.value = value
        self.rarity = rarity
        self.armorValue = armorValue
        self.armorType = armorType
    
    def setArmorType(self) -> ArmorType:
        return self.armorType
    def setArmorType(self, type) -> None:
        self.armorType = type
    def getArmorValue(self) -> int:
        return self.armorValue
    def setArmorValue(self, armor) -> None:
        self.armorValue = armor
        

