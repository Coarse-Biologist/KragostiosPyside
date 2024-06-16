from .buffsClass import Buffs
from .debuffsClass import Debuffs


class onHitEffects:
    def __init__(self, caster_buff : Buffs = None, caster_debuff : Debuffs = None, target_buff  : Buffs = None, target_debuff : Debuffs = None):
        self.caster_buff = caster_buff
        self.caster_debuff = caster_debuff
        self.target_buff = target_buff
        self.target_debuff = target_debuff

        

