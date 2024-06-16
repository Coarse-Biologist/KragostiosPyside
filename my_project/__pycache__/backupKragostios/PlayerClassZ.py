from generalFunctionsZ import* 
import SummonsClassZ as summon
import printSlowlyFunctionZ as slo
from PySide6.QtCore import Signal, QObject


class Player:
    def __init__(self, creature_name: str, player_location: list, max_level_xp: int, xp_progress: int, max_hp: int, hp: int, hp_regen: int, max_mana: int, mana: int, mana_regen: int, player_inv: list, available_actions: list, has_summon:list, learnable_skills: list) -> None:
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
        self.mana_regen = mana_regen #10
        self.player_inv = player_inv #11
        self.available_actions = available_actions #12
        self.has_summon = has_summon #13
        self.learnable_skills = learnable_skills #14

##################### movement handler #################
    #option_print_iter("Whither willst thou go?", ("go North", "go South", "go West", "go East"), 4)


    def move_north(self):
        print("You journey north")
        self.player_location[1] += 1
        print(f"you find yourself at position {self.player_location}")
        return self.player_location

    def move_south (self):
        print("You journey south")
        self.player_location[1] -= 1
        print(f"you find yourself at position {self.player_location}")
        return self.player_location
    
    def move_east (self):
        print("You journey east")
        self.player_location[0] += 1
        print(f"you find yourself at position {self.player_location}")
        return self.player_location
    
    def move_west(self):
        print("You journey west")
        self.player_location[0] -= 1
        print(f"you find yourself at position {self.player_location}")
        return self.player_location

######### inventory handler ############

    def add_inv(self, lootable_item):
        loot_name = list(lootable_item.item_name.keys())[0]
        looted_amount = lootable_item.item_name[loot_name]
        #print(loot_name, looted_amount)
        for inv_item in self.player_inv:
            if loot_name in inv_item:
                inv_item[loot_name] += looted_amount
                break  # Exit the loop once the item is found and updated
        else:
            self.player_inv.append(lootable_item.item_name.copy())  # Append the lootable item if not found

    def display_inv(self):
        for inv_item in self.player_inv:
            print(inv_item)

    def xp_up(self, difficulty_level):
        self.xp_progress += difficulty_level * 10
        if self.xp_progress >= self.max_level_xp:
            self.xp_progress -= self.max_level_xp
            self.level_up()
        elif self.xp_progress == self.max_level_xp:
            self.xp_progress = 0
            self.level_up()
    
    def level_up(self):
            self.level +=1
            self.max_xp *= 2
            self.max_hp +=10
            self.hp_regen += 1
            self.max_mana += 10
            self.mana_regen += 1
            self.choose_new_skill()
            self.choose_stat_increase()

    def name_select(self):
            creature_name = input("What is your name?")
            print(f"Greetings, most exalted {creature_name}")
            return self.creature_name
    
    def add_summon(self, summon_instance):
        self.has_summon.append(summon_instance)
        print(f"The {self.has_summon[0].creature_name} shall aid you in your battles.")


    def choose_stat_increase(self):
        i = len(self.levelable__stats)
        options = 0
        while options < i:
            slo.sloprint(f"Press {options + 1} to improve: {str(self.levelable_stats[options])}.")
            #time.sleep(1)
            options += 1


        while True:
            decision = input("Choose!")
            if decision.isdigit():
                decision = int(decision)
                if i >= decision > 0:
                    if decision == 1:
                        self.max_hp += 20
                        slo.sloprint("Your maximum hitpoints have increased by 20.")
                    elif decision == 2:
                        self.hp_regen += 5
                        slo.sloprint("Your health regeneration has increased by 5.")
                    elif decision == 3:
                        self.mana += 20
                        slo.sloprint("Your maximum mana have increased by 20.")
                    elif decision == 4:
                        self.mana_regen += 5
                        slo.sloprint("Your mana regeneration has increased by 5.")
                else:
                    print("Invalid input. Please select a valid option.")
            else:
                print("Invalid input. Please select a valid option.")

    def choose_new_skill(self):
        i = len(self.learnable_skills)
        options = 0
        if i == 0:
            print("There is nothing more for you to learn at this time.")
            return
        while options < i:
            slo.sloprint(f"Press {options + 1} to learn the skill: {self.learnable_skills[options].skill_name}.")
            #time.sleep(1)
            options += 1
        choice = choice_int_checker(0, options)
        skill_decision = self.learnable_skills[choice].skill_name
        slo.sloprint(f"You have learned {skill_decision}!")
        self.available_actions.append(skill_decision)
        return self.available_actions
    





#player1 = Player("Amy", [0, 0], 100, 10, [{"Item": "Amount"}], ["Kneel", "Stand", "Sit", "Squeal"], [])








#player1= Player (player_name, (0, 0) 100, 0, 100, 100, 1, 100, 5, [], [sklz.simple_attack, sklz.godsmack_attack, sklz.simple_heal], [summon.octopus_fey], [])

#player2= Player (player_name, (0, 0) 100, 0, 100, 100, 1, 100, 5, [], [sklz.simple_attack, sklz.godsmack_attack, sklz.simple_heal], [summon.octopus_fey], [])

#player3= Player (player_name, (0, 0) 100, 0, 100, 100, 1, 100, 5, [], [sklz.simple_attack, sklz.godsmack_attack, sklz.simple_heal], [summon.octopus_fey], [])

#player4= Player (player_name, (0, 0) 100, 0, 100, 100, 1, 100, 5, [], [sklz.simple_attack, sklz.godsmack_attack, sklz.simple_heal], [summon.octopus_fey], [])

#player5= Player (player_name, (0, 0) 100, 0, 100, 100, 1, 100, 5, [], [sklz.simple_attack, sklz.godsmack_attack, sklz.simple_heal], [summon.octopus_fey], [])



















