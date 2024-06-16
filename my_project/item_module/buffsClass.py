from .statusEffects import StatusEffects
from . import myEnums

class Buffs:
    def __init__(self, affected_attributes : myEnums.modifiableAttributes, modifier : int = 0,
                  special_status : StatusEffects = None, duration : int = 0, requirements : list = [], counter_factors : list = []):
        
        self.affected_attributes = affected_attributes
        self. modifier = modifier
        self.special_status = special_status
        self.duration = duration
        self.requirements = requirements
        self.counter_factors = counter_factors
        

    def getAffectedAttributes(self):
        return self.affected_attributes
    
buff1= Buffs(affected_attributes = myEnums.modifiableAttributes.MAX_HP, modifier = 10)
