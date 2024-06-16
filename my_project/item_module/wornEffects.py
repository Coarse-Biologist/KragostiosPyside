from .buffsClass import *
from .debuffsClass import *

class wornEffects:
    def __init__(self, buffs : list = [], debuffs : Debuffs = None):
        self.buffs = buffs
        self.debuffs = debuffs

increase_health10 = wornEffects( buffs = [buff1])