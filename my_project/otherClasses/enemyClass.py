from enum import Enum, auto 
import random
from .skillClass import Skills

class dangerLevel(Enum):
    EASY = auto()
    NORMAL = auto()
    HARD = auto()
    SWEATY = auto()
    NIGHTMARE = auto()

class Enemy:
   def __init__(self, name : str = " ", description : str = " ", max_hp : int = 20,
                 hp : int = 20, available_actions : list = [], danger_level : dangerLevel = dangerLevel.EASY):
       self.name = name
       self.description = description
       self.max_hp = max_hp
       self.hp = hp
       self.available_actions = available_actions
       self.danger_level = danger_level

   @classmethod
   def generate_noob_creature(cls): 
       creature_name = random.choice(cls.noob_creature_name_list)
       description = random.choice (cls.descriptions_list)
       hp = random.randint(10, 50)
       creature_actions = []
       danger_level = random.randint(1, 2)
       if danger_level == 2:
          hp += 20
       enemy_attributes = (creature_name, description, creature_actions, hp, danger_level)
       noob_creatures = cls(*enemy_attributes)
       return noob_creatures
   
   @classmethod
   def generate_unique_creature(cls, creature_id, unique_creatures):
      special_enemies = []
      creature_attributes = cls.special_creature_dict.get(creature_id)
      special_creature = cls(*creature_attributes)
      special_enemies.append(special_creature)
      return special_enemies
    
   @classmethod
   def make_creature_obj(cls, simple_creatures, unique_creatures) -> list:
      enemies = []
      for _ in range(simple_creatures):
         noob_creatures = cls.generate_noob_creature()
         enemies.append(noob_creatures)
      if unique_creatures > 0:
         for _ in range(unique_creatures):
            special_enemies = cls.generate_unique_creature(random.randint(1, 5), unique_creatures)
            enemies.extend(special_enemies)
      return enemies
    
#(f"Name: {creature.creature_name}, Actions: {creature.creature_actions}, Health: {creature.hp}, Danger Level: {creature.danger_level}")

   noob_creature_name_list =["Deformed Baby Goblin", "Ghost Octopusling", "Teenage Orc", "Living Skeleton", "Blood Slime", "Arm Mouth", "Baby Giraff", "Master Rabbit", "Large Frog", "Flaming Pig", "Angry Farmer", "Blood Sloth", "Crawling Hyena", "Old Wolf", "Dagger-wielding-Platypus", "Crippled Spider", "Pus-Spinnling"]

   special_creature_dict = {
      1: ("Alpha Grizzly Octopus", "A fur-covered octopus that prominently displays his single beak.", 40, 40, [], 2),
         2: ("Grizzly Octopus", "A fur-covered octopus that displays his single beak.", 30, 30, [], 1),
            3: ("Beta Grizzly Octopus", "A fur-covered octopus that insecurely displays his single beak.", 25, 25, [], 1),
               4: ("Muscle_Drooler", "A ten foot tall, semihumanoid, bent over its front-hands with a long and pointed tail. The entire body is intensely muscle-bound. The head consists of four eyes located in all quadrants of the head, and a membraneous mouth which extends up to one sixth their body length and contains a cave of jagged bone teeth.", 60, 60, [], 3),
      5: ("Nature Dragon", "A majestic, four-winged god of flight, covered and composed of roots and flowers. The wonderful beast is clothed in a forest.", 100, 100, [], 3)
                     }
   
   descriptions_list = ["A nasty wretch", "A scummy, slimy, bugger", "A snot-faced villain", "Small, hyper-aggressive monster" "A pathetic, little scumbag"]

   def take_damage(self, damage : int):
        self.hp += damage
        return self.hp
   
   def enemy_use_skill(self, skill : Skills, target):
      target.hp -= skill.damage
      skill_result = f"{target} recieved {Skills.damage} damage!"

      return skill_result

