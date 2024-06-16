from .item import Item, ItemRarity
from .item_equipable import *
from enum import Enum, auto


class WeaponType(Enum):
    DAGGER = auto()
    AXE = auto()
    SWORD = auto()

    def __str__(self):
        return self.name.replace("_", " ").lower()

class Weapon(Item, Equipable):
    def __init__(self, name = "", itemType = None, value = 0, rarity = ItemRarity.COMMON, damage = 1, weaponType = None, slot : myEnums.SlotType = None, listOnHitEffects : list = [], listWornEffects : list = []) -> None:
        super(Item, self).__init__()#name, ItemType.WEAPON, value, rarity)
        super(Equipable, self).__init__()
        self.name = name
        self.itemType = itemType
        self.value = value
        self.rarity  = rarity
        self.damage = damage
        self.weaponType = weaponType
        self.slot = slot
        self.listWornEffects = listWornEffects

    def getWeaponType(self) -> WeaponType:
        return self.weaponType
    def setWeaponType(self, type) -> None:
        self.weaponType = type
    def getDamage(self) -> int:
        return self.damage
    def setDamage(self, damage) -> None:
        self.damage = damage

    
