from skillClassZ import *
import SummonsClassZ
from generalFunctionsZ import *
from PlayerClassZ import *
from SummonsClassZ import *
from creatureClassZ import *
from printSlowlyFunctionZ import *
from mapCreatorZ import *
import os 
from PySide6.QtCore import Signal, QObject

class CombatMaster():

    def __init__(self, duration_dict = {}):
        super().__init__()
        self.duration_dict = duration_dict
    
    def add_target (self, target):
        self.duration_dict.setdefault(target, {}) 

    def combatant_intro(self, player_instance, enemy_list):
        if len(enemy_list) == 1:
            sloprint(f"You see a real gnarly lookin' {enemy_list[0].creature_name}!")
        elif len(enemy_list) == 2:
            if enemy_list[0].creature_name == enemy_list[1].creature_name:
                sloprint(f"You see two real gnarly {enemy_list[0].creature_name}" + "s!")
        else:
            intro_string = "You see a real gnarly group:"
            for i, enemy in enumerate(enemy_list):
                if i == len(enemy_list) -1:
                    if is_vowel(enemy.creature_name[0]):
                        intro_string += " and an " + enemy.creature_name + "."
                    else:
                        intro_string += " and a " + enemy.creature_name + "."
                else:
                    if is_vowel(enemy.creature_name[0]):
                        intro_string += " an " + enemy.creature_name + ","
                    else:
                        intro_string+= " A " + enemy.creature_name + ","
            sloprint(intro_string)
            
    def skill_select(self, player_instance):
        min = 0
        actions = []
        for skill in player_instance.available_actions:
            if skill.cost <= player_instance.mana:
                actions.append(skill)
        max = len(actions)
        i = 0
        while i < max:
            for item in actions:
                if isinstance(item, Skill):
                    sloprint(f"Press {i + 1} to use {item.skill_name}.")
                    i += 1
                elif isinstance(item, Creature):
                    sloprint(f"Press {i + 1} to summon a {item.creature_name}.")
                    i += 1
        choice = choice_int_checker(min,max) - 1
        choice = actions[choice]
        return choice # returns the INDEX of a skill or summon selected by the player 
    
    def target_select(self, combatants_list, skill_instance):
        combatant_names = []
        for combatant in combatants_list:
            if isinstance(combatant, Summon):
                summon_name = (f"{combatant.creature_name}.(Your Summon)")
                combatant_names.append(summon_name)
            elif isinstance(combatant, Creature):
                combatant_names.append(combatant.creature_name)
            elif isinstance(combatant, Player):
                 combatant_names.append("Yourself")
        choice = noun_print_iter("At whom do you direct this skill?", combatant_names, len(combatants_list))
        target = combatants_list[choice - 1]
        self.add_target(target)
        if isinstance (skill_instance, str):
            pass
        else:
            self.skill_duration_adder(target, skill_instance)
            sloprint(f"You have used {skill_instance.skill_name} on {combatant_names[choice - 1]}.")
        return target
        
    def combatants_list_create(self, player_instance, enemy_list):
        self.combatants_list = []
        for enemy in enemy_list:
            self.combatants_list.append(enemy)
        if len(player_instance.has_summon) != 0:
            for summon in player_instance.has_summon:
                self.combatants_list.append(summon)
        self.combatants_list.append(player_instance)
        return self.combatants_list
    
    def effect_handler(self, caster, skill_instance, target, combatants_list, shuffled_turns): 
        skill_effects_dict = skill_instance.skill_at_checker()
        if "duration" in skill_effects_dict:
            self.skill_duration_adder(skill_instance, target)
        if "cost" in skill_effects_dict:
            self.lose_mana(caster, skill_instance)
        if "damage" in skill_effects_dict:
            if "lingering damage" in skill_effects_dict:  
                self.cause_all_damage(skill_instance, target, combatants_list, shuffled_turns)
            else: 
                self.cause_damage(skill_instance, target, combatants_list, shuffled_turns)
        elif "lingering damage" in skill_effects_dict and "damage" not in skill_effects_dict:
            self.cause_lingering_damage(skill_instance, target, combatants_list, shuffled_turns)
        if "heal" in skill_effects_dict:
            self.heal(skill_instance, target)
        if "buff" in skill_effects_dict:
            pass
            #self.apply_buff(skill_instance, target)
        if "debuff" in skill_effects_dict:
            pass
            #self.apply_debuff(skill_instance, target)
        if "push" in skill_effects_dict:
            pass

    def skill_duration_adder(self, target, skill_instance):  ###########!!!!!!! fehler
        counter = skill_instance.duration
        name = skill_instance.skill_name
        self.duration_dict[target].setdefault(name, counter)
        sloprint(self.duration_dict[target])
        return self.duration_dict[target]
        
    def decrement_duration(self, skill_instance):
        for player in self.duration_dict.items():
            for skill, duration in player.items():
                if player[skill] == 1:
                    self.duration_dict.pop(skill)
                else:
                    skill[duration] -= 1

    def lose_mana(self, caster, skill_instance):
        if isinstance(caster, Player):
            caster.mana -= skill_instance.cost
            sloprint(f"You used {skill_instance.cost} mana, and have {caster.mana} remaining.")
            return caster # player instance bcuz only one that loses mana

    def cause_damage(self, skill_instance, target, combatants_list, shuffled_turns):
        target.hp -= skill_instance.damage
        sloprint(f"{skill_instance.skill_name} caused {skill_instance.damage}!")
        if target.hp <= 0:
            if target == combatants_list[-1]:
                sloprint("You have succomed to your wounds and fallen asleep in death.")
                combatants_list.remove(target)
                shuffled_turns.remove(target)
            elif isinstance(target, Summon):
                sloprint(f"Your summon, {target.creature_name} has tragically fallen asleep in the wicked embrace of death")
                combatants_list.remove(target)
                shuffled_turns.remove(target)
                for obj in combatants_list:
                    if isinstance(obj, Player):
                        obj.has_summon.remove(target)
            elif isinstance(target, Creature):
                sloprint(f"HAHAHAHA! Your pathetic enemy, {target.creature_name} is dead, never to awaken again.")
                combatants_list.remove(target)
                shuffled_turns.remove(target)

        return target, combatants_list
    
    def cause_lingering_damage(self, skill_instance, target,  combatants_list, shuffled_turns):
        target.hp -= skill_instance.lingering_damage
        sloprint(f"{skill_instance.skill_name} caused {skill_instance.lingering_damage} extra lingering damage!")
        if target.hp <= 0:
            if target == 'self':
                sloprint("You have succomed to your wounds and fallen asleep in death.")
                combatants_list.remove(target)
                shuffled_turns.remove(target)
            elif isinstance(target, Summon):
                sloprint(f"Your summon, {target.creature_name} has tragically fallen asleep in the wicked embrace of death")
                combatants_list.remove(target)
                shuffled_turns.remove(target)
                for obj in combatants_list:
                    if isinstance(obj, Player):
                        obj.has_summon.remove(target)
            elif isinstance(target, Creature):
                sloprint(f"HAHAHAHA! Your pathetic enemy, {target.creature_name} is dead, never to awaken again.")
                combatants_list.remove(target)
                shuffled_turns.remove(target)
        return target, combatants_list

    def cause_all_damage(self, skill_instance, target, combatants_list, shuffled_turns):
        target.hp -= skill_instance.damage + skill_instance.lingering_damage
        if isinstance (target, Player):
            sloprint(f"{target.creature_name} suffered {skill_instance.damage + skill_instance.lingering_damage} damage!")
        else:
            sloprint(f"{target.creature_name} suffered {skill_instance.damage + skill_instance.lingering_damage} damage!")
        if target.hp <= 0:
            if isinstance(target, Player):
                sloprint("You have succomed to your wounds and fallen asleep in death.")
                combatants_list.remove(target)
                shuffled_turns.remove(target)
            elif isinstance(target, Summon):
                sloprint(f"Your summon, {target.creature_name} has tragically fallen asleep in the wicked embrace of death")
                combatants_list.remove(target)
                shuffled_turns.remove(target)
                for obj in combatants_list:
                    if isinstance(obj, Player):
                        obj.has_summon.remove(target)
            elif isinstance(target, Creature):
                sloprint(f"HAHAHAHA! Your pathetic enemy, {target.creature_name} is dead, never to awaken again.")
                combatants_list.remove(target)
                sloprint(combatants_list)
                shuffled_turns.remove(target)

        return target,  combatants_list  

    def heal(self, skill_instance, target):
        target.hp += skill_instance.heal
        return target
        
    def turn_handler(self, combatants_list, the_environment):
        player = combatants_list[-1]
        shuffled_turns = combatants_list.copy()
        random.shuffle(shuffled_turns)
        while any(isinstance(combatant, Creature) for combatant in combatants_list):
            for combatant in shuffled_turns:
                if isinstance(combatant, Player) and combatant.hp <= 0:
                    sloprint("You lose")
                    return
                if player.hp > 0:
                    if len(player.has_summon) + 1 == len(combatants_list):
                        sloprint("you win")
                        return
                    else:
                        self.turn_type_decider(combatant, combatants_list, shuffled_turns, the_environment)
        sloprint("You win?")

    def turn_type_decider(self, combatant, combatants_list, shuffled_turns, the_environment):
        if isinstance(combatant, Player):
            self.player_turn(combatant, combatants_list, shuffled_turns)
        elif isinstance(combatant, Summon):
            if combatant.controlled == False:
                self.autonomous_summon_turn(combatant, combatants_list, shuffled_turns, the_environment)
            else:
                self.controlled_summon_turn(combatant, combatants_list, shuffled_turns, the_environment)
        elif isinstance(combatant, Creature):
            self.enemy_turn(combatant, combatants_list, shuffled_turns, the_environment)
            return shuffled_turns
    
    def player_turn(self, combatant, combatants_list, shuffled_turns):
        sloprint("It is your turn to make a move!")
        chosen_skill = self.skill_select(combatant)
        caster = combatants_list[-1]                    ##'or backwards? and why
        target = self.target_select(combatants_list, chosen_skill)
        self.effect_handler(caster, chosen_skill, target, combatants_list, shuffled_turns)

    def autonomous_summon_turn(self, combatant, combatants_list, shuffled_turns, the_environment):
        sloprint("It is your summon's turn to make a move!")
        caster = combatant                          #or backwards? and why?
        possible_skills = combatant.creature_actions
        chosen_skill = random.choice(possible_skills)
        targets = []
        for potential_target in combatants_list:
            if isinstance(potential_target, Summon):
                pass
            elif isinstance(potential_target, Creature):
                targets.append(potential_target)
        if len(targets) == 0:
            return 
        target = random.choice(targets)                 # herere
        combatant = caster              # or caster = combatant?
        if isinstance(chosen_skill, str):
            death = functionSkills.precipace_throw(combatant, target, the_environment)
            if death == True:
                shuffled_turns.remove(target)
                combatants_list.remove(target)
                return shuffled_turns, combatants_list
        else:
            sloprint(f"{combatant.creature_name} (Your summon) used {chosen_skill.skill_name} on {target.creature_name}!")
            self.effect_handler(caster, chosen_skill, target, combatants_list, shuffled_turns)

    def controlled_summon_turn(self, combatant, combatants_list, shuffled_turns, the_environment):
        sloprint("It is your summon's turn to make a move!")
        min = 0
        max = len(combatant.creature_actions)
        i = 0
        while i < max:
            for item in combatant.creature_actions:
                if isinstance(item, str):
                    sloprint(f"Press {i + 1}: command summon to use {item}.")
                    i += 1
                if isinstance(item, Skill):
                    sloprint(f"Press {i + 1}: command summon to use {item.skill_name}.")
                    i += 1
                elif isinstance(item, Creature):
                    sloprint(f"Press {i + 1} to summon a {item.creature_name}.")
                    i += 1
        choice = choice_int_checker(min,max) - 1
        chosen_skill = combatant.creature_actions[choice]
        target = self.target_select(combatants_list, chosen_skill)
        if isinstance(chosen_skill, str):
            death = functionSkills.precipace_throw(combatant, target, the_environment)
            if death == True:
                shuffled_turns.remove(target)
                combatants_list.remove(target)
                return shuffled_turns, combatants_list 
            else:
                return       
        else:
            self.effect_handler(combatant, chosen_skill, target, combatants_list, shuffled_turns)

    def enemy_turn(self, combatant, combatants_list, shuffled_turns, the_environment):
        print(combatant.__class__)
        sloprint(f"It is {combatant.creature_name} turn to make a move!")
        caster = combatant
        possible_skills = combatant.creature_actions
        chosen_skill = random.choice(possible_skills)
        target_list = []
        for potential_target in combatants_list:
            if potential_target.__class__ is Summon:
                target_list.append(potential_target)
            if potential_target.__class__ is Player:
                target_list.append(potential_target)
            else:
                pass
        target = random.choice(target_list)
        if isinstance(chosen_skill, str):
            death = functionSkills.precipace_throw(combatant, target, the_environment)
            if death == True:
                shuffled_turns.remove(target)
                combatants_list.remove(target)
                return shuffled_turns, combatants_list
        if isinstance(target, Summon):
            sloprint(f"{combatant.creature_name} used {chosen_skill.skill_name} on {target.creature_name}!")
            self.effect_handler(caster, chosen_skill, target, combatants_list, shuffled_turns)
        elif isinstance(target, Player):
            sloprint(f"{combatant.creature_name} used {chosen_skill.skill_name} on {target.creature_name}!")
            self.effect_handler(caster, chosen_skill, target, combatants_list, shuffled_turns)
        elif isinstance(target, Creature):
            sloprint(f"{combatant.creature_name} used {chosen_skill.skill_name} on {target.creature_name}!")
            self.effect_handler(caster, chosen_skill, target, combatants_list, shuffled_turns)


    def combat_loop(self):
        #self.printSignal.emit("Sit once")
        self.printSignal.emit("Sit twice")

        os.system('cls' if os.name == 'nt' else 'clear')
        player1= Player("", (0, 0), 100, 0, 100, 100, 1, 100, 100, 5, [], [skill1, skill2, skill3], [], [])
        player1.creature_name = player1.name_select()
        print("Your being tingles with the energy of eminent danger! There is an enemy nearby!")
        the_environment = map1.check_environment()
        my_summon = Creature.make_creature_obj(1, 0)
        Summon.summon_made_creature(player1, my_summon)
        enemy_list = Creature.make_creature_obj(0, 1)
        self.combatant_intro(player1, enemy_list)
        combatants_list = self.combatants_list_create(player1, enemy_list)
        for combatant in combatants_list:
            if isinstance(combatant, Creature):
                combatant.add_environment_use(the_environment)
        self.turn_handler(combatants_list, the_environment)
        return

#squealfest = CombatMaster({})

#squealfest.combat_loop()
