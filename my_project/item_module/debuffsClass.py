from .statusEffects import StatusEffects, myEnums

class Debuffs:
    def __init__(self, affected_attributes : myEnums.modifiableAttributes, modifier : list = [],
                  special_status : StatusEffects = None, duration : int = 0, requirements : list = [], counter_factors : list = []):
        self.affected_attributes = affected_attributes
        self. modifier = modifier
        self.special_status = special_status
        self.duration = duration
        self.requirements = requirements
        self.counter_factors = counter_factors