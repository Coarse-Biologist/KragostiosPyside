import skillClassZ as sklz
import random
from printSlowlyFunctionZ import *


class Creature:

   def __init__(self, creature_name, description: str, creature_actions: list, hp: int, danger_level: int):
        self.creature_name = creature_name
        self.description = description
        self.creature_actions = creature_actions
        self.hp = hp
        self.danger_level = danger_level
      
   @classmethod
   def generate_noob_creature(cls): 
      creature_name = random.choice(cls.noob_creature_name_list)
      description = random.choice (cls.descriptions_list)
      hp = random.randint(10, 50)
      creature_actions = [sklz.skill1]
      danger_level = random.randint(1, 2)
      if danger_level == 2:
         hp += 20
      enemy_attributes = (creature_name, description, creature_actions, hp, danger_level)
      noob_creatures = cls(*enemy_attributes)
      return noob_creatures
   
   @classmethod
   def special_creature_generator(cls, creature_id, specials):
      special_enemies = []
      x= 0
      while x < specials:
         creature_attributes = cls.special_creature_dict.get(creature_id)
         special_creature = cls(*creature_attributes)
         special_enemies.append(special_creature)
         x += 1
      return special_enemies
   
   @classmethod
   def make_creature_obj(cls, noobs, specials) -> list:
      enemies = []
      for _ in range(noobs):
         noob_creatures = cls.generate_noob_creature()
         enemies.append(noob_creatures)
      ##for creature in enemies:
          #print(f"Name: {creature.creature_name}, Actions: {creature.creature_actions}, Health: {creature.hp}, Danger Level: {creature.danger_level}")
      if specials > 0:
         for _ in range(specials):
            special_enemies = cls.special_creature_generator(random.randint(1, 5), specials)
            enemies.extend(special_enemies)
      return enemies


   def add_environment_use(self, the_environment):
      #self.creature_actions.append(sklz.push())

       # creatureClass skill
      #if the_environment == "jungle":
      #    self.creature_actions.append(sklz.climb())
      if the_environment == "cliffs":
         self.creature_actions.append("precipacethrow")
      #elif the_environment == "forest":
      #   self.creature_actions.append(sklz.climb())
      #elif the_environment == "canyons":
      #   self.creature_actions.append(sklz.push())
      #elif the_environment == "grasslands":
      #   pass
      #elif the_environment == "icy terrain":
      #   self.creature_actions.append(sklz.push())
      #elif the_environment == "muddy terrain":
      #   self.creature_actions.append(sklz.push())
      elif the_environment == "subterranean caves":
         self.creature_actions.append("precipacethrow")
      elif the_environment == "quick sand":
         self.creature_actions.append("precipacethrow")
      #elif the_environment == "barren wasteland":
      #   pass
      #elif the_environment == "cactus-filled desert":
      #   self.creature_actions.append(sklz.push())
      #elif the_environment == "deserted village":
      #   pass
      #elif the_environment == "a slowly flowing river":
      #   self.creature_actions.append(sklz.push())
      elif the_environment == "a treacherously fleet and rocky river":
         self.creature_actions.append("precipacethrow")
         #   pass

   special_creature_dict = {
      1: ("Alpha Grizzly Octopus", "A fur-covered octopus that prominently displays his single beak.", [sklz.skill1, sklz.skill6], 40, 2),
         2: ("Grizzly Octopus", "A fur-covered octopus that displays his single beak.", [sklz.skill1, sklz.skill6], 30, 1),
            3: ("Beta Grizzly Octopus", "A fur-covered octopus that insecurely displays his single beak.", [sklz.skill1, sklz.skill6], 25, 1),
               4: ("Muscle_Drooler", "A ten foot tall, semihumanoid, bent over its front-hands with a long and pointed tail. The entire body is intensely muscle-bound. The head consists of four eyes located in all quadrants of the head, and a membraneous mouth which extends up to one sixth their body length and contains a cave of jagged bone teeth.", [sklz.skill1], 60, 3),
      5: ("Nature Dragon", "A majestic, four-winged god of flight, covered and composed of roots and flowers. The wonderful beast is clothed in a forest.", [sklz.skill1], 100, 3)
                     }

   noob_creature_name_list =["Deformed Baby Goblin", "Ghost Octopusling", "Teenage Orc", "Living Skeleton", "Blood Slime", "Arm Mouth", "Baby Giraff", "Master Rabbit", "Large Frog", "Flaming Pig", "Angry Farmer", "Blood Sloth", "Crawling Hyena", "Old Wolf", "dagger-wielding-Platypus", "Crippled Spider", "Pus-Spinnling"]
   
   descriptions_list = ["A nasty wretch", "A scummy, slimy, bugger", "A snot-faced villain", "Small, hyper-aggressive monster" "A pathetic, little scumbag"]


class functionSkills:
    def __init__(self):
        pass
    
    
    @classmethod
    def precipace_throw(cls, combatant, target, the_environment): 
         sloprint(f"{combatant.creature_name} is considering whether this an honorable fight. \n {combatant.creature_name} decided that it is not! \n {combatant.creature_name} is trying to pick up {target.creature_name}!")
         pickup_roll = random.random()
         pickup_success = False
         if isinstance(target, Creature):
            if target.danger_level > combatant.danger_level:
               if pickup_roll > .6:
                  pickup_success = True
               else:
                  pickup_success = False
            elif target.danger_level < combatant.danger_level:
                  if pickup_roll > .4:
                     pickup_success = True
                  else:
                     pickup_success = False 
         else:
            if pickup_roll > .8:
                  pickup_success = True
         if pickup_success == True:
            sloprint(f"Oh my gordon! {combatant.creature_name} grabbed the {target.creature_name} and is carrying him somewhere! \n {combatant.creature_name} just threw {target.creature_name} into {the_environment}!")
            print("Hes dead! There goes the loot!")
         else:
            print(f"{combatant.creature_name} failed and dropped {target.creature_name}!")