from . import myEnums

class Equipable:
    def __init__(self,  listOnHitEffects : list = [], listWornEffects : list = [], slot : myEnums.SlotType = None):
        self.listOnHitEffects = listOnHitEffects 
        self.listWornEffects = listWornEffects
        self.slot = slot

# slot
    def getSlotType(self) -> myEnums.SlotType:
        return self.slot
    def setSlotType(self, slot) -> None:
        self.slot = slot

# on hit
    def hasOnHit(self) -> None:
        return len(self.listOnHitEffects) > 0
    def getOnHitEffects(self) -> list: 
        return self.listOnHitEffects
    def setOnHitList(self, listEffects : list) -> None:
        self.listOnHitEffects = listEffects
    def addOnHitEffect(self, newEffect) -> None: 
        if isinstance(newEffect): 
            self.listOnHitEffects.append()
        elif isinstance(newEffect, list):
            self.listOnHitEffects.extend(newEffect)

# worn effects
    def hasWornEffects(self) -> bool:
        return len(self.listWornEffects) > 0   
    def getWornEffects(self) -> list:
        return self.listWornEffects
    def setWornList(self, listEffects : list) -> None:
        self.listWornEffects = listEffects

    def addWornEffect(self, newEffect) -> None: 
        if isinstance(newEffect):   
            self.listWornEffects.append()
        elif isinstance(newEffect, list):
            self.listWornEffects.extend(newEffect)

    