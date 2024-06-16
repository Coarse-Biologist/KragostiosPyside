from . import myEnums

class StatusEffects:
    def __init__(self, name : str = " ", effect_relevence : myEnums.effectRelevence = None, description : str = " "):
        self.name = name
        self.effect_relevence = effect_relevence
        self.description = description

        status1 = StatusEffects(name = "stunned", effect_relevence = myEnums.effectRelevence.TURN_START, description = "The being cannot move")
        status2 = StatusEffects(name = "frozen", effect_relevence = myEnums.effectRelevence.TURN_START, description = "The beings muscles are frozen solid")
        status3 = StatusEffects(name = "entangled", effect_relevence = myEnums.effectRelevence.ABILITY_SELECT, description = "The being is covered in and ensnared by plant vines")
        status4 = StatusEffects(name = "electrified",  effect_relevence = myEnums.effectRelevence.TURN_START, description = "The being's muscles are exploding with energy and acting eradically.")
        status5 = StatusEffects(name = "insane", effect_relevence = myEnums.effectRelevence.ABILITY_SELECT, description = "The being has been driven to complete madness")
        status6 = StatusEffects(name = "frenzied", effect_relevence = myEnums.effectRelevence.TARGET_SELECT, description = "The being's blood boils with uncontrollable panic and rage at whoever is nearest.")
        status7 = StatusEffects(name = "mind-controlled", effect_relevence = myEnums.effectRelevence.TURN_START, description = "The beings will is replaced by that of another.")
        status8 = StatusEffects(name = "paralyed", effect_relevence = myEnums.effectRelevence.TURN_START, description = "The being is unable to move a muscle.")
        status9 = StatusEffects(name = "wet", description = "The being is soaking wet.")
        status10 = StatusEffects(name = "demoralized", effect_relevence = myEnums.effectRelevence.TURN_START, description = "The being hat kein Bock mehr.")
        status11 = StatusEffects(name = "euphoric", effect_relevence = myEnums.effectRelevence.TURN_START, description = "The being suddenly overcomes a euphoric feeling that makes it feel like it can conquer the world.")
        status12 = StatusEffects(name = "weakened", effect_relevence = myEnums.effectRelevence.ON_HIT, description = "THe beings strength has left and been replaced by sluggishness")

        all_statusEffects =  {}
        statuses = {status1.name : status1, status2.name : status2,
                    status3.name : status3, status4.name : status4,
                    status5.name : status5, status6.name : status6,
                    status7.name : status7, status8.name : status8,
                    status9.name : status9, status10.name : status10,
                    status11.name : status11, status12.name : status12}
        
        all_statusEffects.update(statuses)
