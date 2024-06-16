from enum import Enum, auto

class ItemType(Enum):
    WEAPON = auto()
    ARMOR = auto()
    POTION = auto()
    SCROLL = auto()
    MISCELANEOUS = auto()

    def __str__(self):
        return self.name.replace("_", " ").lower()
    
class ItemRarity(Enum):
    COMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()

    def __str__(self):
        return self.name.replace("_", " ").lower()

class Item:
    def __init__(self, name = "", type : ItemType = None, value = 0, sellable: bool = True, rarity = ItemRarity.COMMON) -> None:
        self.name = name
        self.type = type
        self.value = value
        self.sellable = sellable
        self.rarity = rarity
 
    def getName(self) -> str:
        return self.name
    def setName(self, name : str) -> None:
        self.name = name
    def getType(self) -> ItemType:
        return self.type
    def setType(self, type : ItemType) -> None:
        self.type = type
    def isSellable(self) -> bool:
        return self.sellable
    def setSellable(self, value : bool) -> None:
        self.sellable = value
