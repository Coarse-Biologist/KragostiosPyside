from ..item_module import onHitEffects, statusEffects


class Skills():
    def __init__(self, cost : int = 0, damage : int = 0, effects : statusEffects = None):
        self.cost = cost
        self.damage = damage
        self.effects = effects


    def getdamage(self):
        return self.damage
    
    def getCost(self):
        return self.cost
    
    def getEffects(self):
        return self.effects
    
skill1 = Skills(cost = 1, damage = 1, effects = None)

    