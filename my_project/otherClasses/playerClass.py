
from ..item_module import item_storage
from ..item_module import onHitEffects 
from ..item_module import item_equipable 
from ..item_module import myEnums
from ..item_module import statusEffects
from .skillClass import Skills

class Player:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, creature_name: str = "", player_location: list = [0,0], player_level: int = 1, max_level_xp: int = 100, xp_progress: int = 0, max_hp: int = 100, hp: int = 100, hp_regen: int = 1, max_mana: int = 100, mana: int = 100, mana_regen: int = 1, player_inv: list = [], equipped_items : list = [], armor_value : int = 0, available_actions: list =  [], has_summon:list = [], learnable_skills: list = [], classy: str = "") -> None:
        super().__init__()
        self.creature_name = creature_name #1
        self.player_location = player_location #2
        self.max_level_xp = max_level_xp #3
        self.xp_progress = xp_progress #4
        self.max_hp = max_hp #5
        self.hp = hp #6
        self.hp_regen = hp_regen #7
        self.max_mana = max_mana #8
        self.mana = mana #9
        self.mana_regen = mana_regen #10-
        self.player_inv = player_inv #11
        self.available_actions = available_actions #12
        self.has_summon = has_summon #13
        self.learnable_skills = learnable_skills #14
        self.classy = classy #15
        self.player_level = player_level #16 (#3)
        self.equipped_items = equipped_items #17
        self.armor_value = armor_value #18
    
##################### movement handler #################
    #option_print_iter("Whither willst thou go?", ("go North", "go South", "go West", "go East"), 4)

    def move_north(self):
        self.player_location[1] += 1
        return self.player_location

    def move_south (self):
        self.player_location[1] -= 1
        return self.player_location
    
    def move_east (self):
        self.player_location[0] += 1
        return self.player_location
    
    def move_west(self):
        self.player_location[0] -= 1
        return self.player_location
    
    def get_location(self):
        return self.player_location

######### inventory handler ############

    def add_inv(self, lootable_item):
        loot_name = list(lootable_item.item_name.keys())[0]
        looted_amount = lootable_item.item_name[loot_name]
        for inv_item in self.player_inv:
            if loot_name in inv_item:
                inv_item[loot_name] += looted_amount
                break
            else:
                self.player_inv.append(lootable_item.item_name.copy())  # Append the lootable item if not found

    def equip_item(self, equipable_item):
        item_slot = item_equipable.equipable_item.getSlotType()
        for item in self.equipped_items:
            if item_slot == item.slot:
                self.armor_value -= item.armorValue
                self.equipped_items.remove(item)
                self.equipped_items.append(equipable_item)
        self.armor_value += equipable_item.armorValue
        self.handleWornEffects(equipable_item)
                
    def add_summon(self, summon_instance):
        self.has_summon.append(summon_instance)
        print(f"The {self.has_summon[0].creature_name} shall aid you in your battles.")

    def display_inv(self):
        for inv_item in self.player_inv:
            print(inv_item)

    def name_select(self):
            self.creature_name = input("question!!! What is your name?")
            #print(f"Greetings, most exalted {creature_name}")
            return self.creature_name

    def xp_up(self, difficulty_level):
        self.xp_progress += difficulty_level * 10
        if self.xp_progress >= self.max_level_xp:
            self.xp_progress -= self.max_level_xp
            self.level_up()
        elif self.xp_progress == self.max_level_xp:
            self.xp_progress = 0
            self.level_up()

    def choose_new_skill(self):
        i = len(self.learnable_skills)
        options = 0
        if i == 0:
            print("There is nothing more for you to learn at this time.")
            return
        while options < i:
            print(f"Press {options + 1} to learn the skill: {self.learnable_skills[options].skill_name}.")
            options += 1

        choice = 1 #choice_int_checker(0, options)
        skill_decision = self.learnable_skills[choice].skill_name
        print(f"You have learned {skill_decision}!")
        self.available_actions.append(skill_decision)
        return self.available_actions
    
    def choose_stat_increase(self):
        i = len(self.levelable__stats)
        options = 0
        while options < i:
            print(f"Press {options + 1} to improve: {str(self.levelable_stats[options])}.")
            #time.sleep(1)
            options += 1
        while True:
            decision = input("Choose!")
            if decision.isdigit():
                decision = int(decision)
                if i >= decision > 0:
                    if decision == 1:
                        self.max_hp += 20
                        print("Your maximum hitpoints have increased by 20.")
                    elif decision == 2:
                        self.hp_regen += 5
                        print("Your health regeneration has increased by 5.")
                    elif decision == 3:
                        self.mana += 20
                        print("Your maximum mana have increased by 20.")
                    elif decision == 4:
                        self.mana_regen += 5
                        print("Your mana regeneration has increased by 5.")

                else:
                    print("Invalid input. Please select a valid option.")
            else:
                print("Invalid input. Please select a valid option.")

    def level_up(self):
            self.player_level +=1
            self.max_level_xp *= 2
            self.max_hp +=10
            self.hp_regen += 1
            self.max_mana += 10
            self.mana_regen += 1
            self.choose_new_skill()
            self.choose_stat_increase()

    def set_name(self, name):
        self.creature_name = name
        
    def get_name(self):
        return self.creature_name
    
    def player_attribute_dict(self):
        player_attribute_dict = {}
        player_attribute_dict.setdefault("Player Name:", f"{self.creature_name}")
        player_attribute_dict.setdefault("Class:", f"{self.classy}")
        player_attribute_dict.setdefault("Location:", f"{str(self.player_location)}")
        player_attribute_dict.setdefault("Level:", f"{self.player_level}")
        player_attribute_dict.setdefault("Experience Points", f"{self.xp_progress} / {self.max_level_xp}")
        player_attribute_dict.setdefault("Hitpoints:", f"{self.hp} / {self.max_hp}")
        player_attribute_dict.setdefault("Hitpoint regeneration:", f"{self.hp_regen}")
        player_attribute_dict.setdefault("Mana:", f"{self.mana} / {self.max_mana}")
        player_attribute_dict.setdefault("Mana regeneration:", f"{self.mana_regen}")
        player_attribute_dict.setdefault("Known Skills:", f"{tuple(self.available_actions)}")
        player_attribute_dict.setdefault("Available Summons", f"{self.has_summon}")

        return player_attribute_dict
    
    def handleWornEffects(self, equipable_item):
        worn_list  = item_equipable.equipable_item.getWornList()
        for effect in worn_list:
            if isinstance(effect, onHitEffects.Buffs):
                affected_attribute = myEnums.getAffectedAttributes()
                if affected_attribute == myEnums.modifiableAttributes.MAX_HP:
                    self.max_hp += equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.HP:
                    self.hp += equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.HP_REGEN:
                    self.hp_regen += equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.MAX_MANA:
                    self.max_mana += equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.MANA:
                    self.mana += equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.MANA_REGEN:
                    self.mana_regen += equipable_item.modifier
                else: 
                    pass
            elif isinstance(effect, onHitEffects.Debuffs):
                affected_attribute = myEnums.getAffectedAttributes()
                if affected_attribute == myEnums.modifiableAttributes.MAX_HP:
                    self.max_hp -= equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.HP:
                    self.hp -= equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.HP_REGEN:
                    self.hp_regen -= equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.MAX_MANA:
                    self.max_mana -= equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.MANA:
                    self.mana -= equipable_item.modifier
                elif affected_attribute == myEnums.modifiableAttributes.MANA_REGEN:
                    self.mana_regen -= equipable_item.modifier
                else: 
                    pass
            elif isinstance(effect, statusEffects):
                pass

    def take_damage(self, damage : int):
        self.hp += damage
        return self.hp
    
    def apply_Skill_cost(self, Skills):
        self.mana -= Skills.cost

    def get_player(self):
        return self.player
        