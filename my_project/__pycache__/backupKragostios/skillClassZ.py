import random
class Skill:
    def __init__(self, skill_name: str, description: str, duration: int, cost: int, damage: int, lingering_damage: int, heal: int,buff: list, debuff: list, skill_attributes_dict: dict):
        
        self.skill_name = skill_name #1
        self.description = description #2
        self.duration = duration #3
        self.cost = cost #4
        self.damage = damage #5
        self.lingering_damage = lingering_damage #6
        self.heal = heal #7
        self.buff = buff #8
        self.debuff = debuff #9
        self.skill_attributes_dict = (f"Skill name: {skill_name}\n Description: {description}\n Duration: {duration} turns \n Cost: {cost} mana points \n Damage: {damage} \n Lingering damage: {lingering_damage}\n Healing: {heal}\n Buffs applied: {buff}\n Debuffs applied: {debuff}") #10
    def __str__(self):
          return self.skill_attributes_dict
    
    # debuff library
    
    def skill_at_checker(self):
        skill_charactaristic_dict = {}
        if self.duration >= 2:
            skill_charactaristic_dict.setdefault("duration", self.duration)
        if self.cost > 0:
            skill_charactaristic_dict.setdefault("cost", self.cost)
        if self.damage > 0:
            skill_charactaristic_dict.setdefault("damage", self.damage)
        if self.lingering_damage > 0:
            skill_charactaristic_dict.setdefault("lingering damage", self.lingering_damage)
        if self.heal > 0:
            skill_charactaristic_dict.setdefault("heal", self.heal)
        if len(self.buff) > 0:
            skill_charactaristic_dict.setdefault("buff", (self.buff))
        if len(self.debuff) > 0:
            skill_charactaristic_dict.setdefault("debuff", (self.debuff))
        if self.skill_name == "push":
            skill_charactaristic_dict.setdefault("push", None)
        #print(self.skill_attributes_dict)
        return skill_charactaristic_dict     
         



### buffs ###
def climb(self): #buff function
    pass # decrease chance of being hit

### debuffs ###
def push(self):
    pass
    print("smells")


#skill library (needs to be organized and expanded)
        
skill1 = Skill("Attack", "A simple, but quick attack.", 1, 0, 5, 0, 0, [], [], {})

skill2 = Skill("Obliterate", "A divine strike.", 1, 100, 100, 0, 0, [], [], {})

skill3 = Skill("Touch of the healer", "A simple healing spell", 1, 20, 0, 0, 10, [], [], {})
skill4 = Skill("Summon Living Fire", "Fire and intellect leave you to become an independent, warming force", 20, 60, 0, 0, 0, [], [], {})
    
skill5 = Skill("Obscure", "An ability that are wraps the caster in shadow and obscurity", 5, 60, 0, 0, 10, [], ["lower_hitchance1"], {})

skill6 = Skill("Tentacle Choke", "An ability of many-armed monsters to wrap their tentacles around their target and squeezes with fearful force.", 1, 10, 20, 0, 0, [], [], {} ) #octopus_fey and similar creatures have access.

creature_climb = Skill("Climb", "Use the environment to ascend to high ground.", 99, 0, 0, 0, 0, [climb], [], {})

creature_push = Skill("Push", "Give an all-out shove. What is behind the push? Whats behind the target?", 1, 0, 0, 0, 0, [], [], {})

def push(self):
    print("smells")