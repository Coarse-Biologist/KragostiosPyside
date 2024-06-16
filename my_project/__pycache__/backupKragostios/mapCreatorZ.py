import random 
import time


class Map:

    def __init__(self, quest_location, enemy_location_list = [], merchant_location = [], loot_location = []) -> None:
        self.enemy_location_list = enemy_location_list
        self.merchant_location = merchant_location
        self.loot_location = loot_location
        self.all_locations = dict()
        self.all_locations.setdefault("Merchant", merchant_location)
        self.all_locations.setdefault("Enemy", merchant_location)
        self.all_locations.setdefault("Loot", merchant_location)
        self.quest_location = []
    #    self.x_boundary = (-100, 100)
    #    self.y_boundary = ()

    def check_environment(self): # map Class function
        environment_possibilities = ("jungel", "cliffs", "forest", "canyons", "grasslands", "icy terrain", "muddy terrain", "subterranean caves", "quick sand", "barren wasteland", "cactus-filled desert", "deserted village", "a slowly flowing river", "a treacherously fleet and rocky river")
        the_environment = random.choice(environment_possibilities)
        print(f"Ah, {the_environment}! What a place for a fight!")
        return the_environment

    def get_locations(self, amount, location_type : str) -> list: # dont allow amount to be larger than available locations/3
        dict1 = {}
        #self.location_type = location_type
        i = amount
        while i > 0:
            loc_x = random.randint(-1,1)
            loc_y = random.randint(-1,1)
            vacant = True
            for key in self.all_locations.keys():
                if (loc_x, loc_y) in self.all_locations[key]:
                    vacant = False
                    break   
            if vacant == True:
                self.all_locations[location_type].append((loc_x, loc_y))
                print(f"{location_type} at ({loc_x}, {loc_y})")
                i -= 1
        return location_type

    def compareLocations(self, player_location: tuple, all_locations):
        if player_location in all_locations["Enemy"]:
            return "danger"
        elif player_location in all_locations["Merchant"]:
            return "merchant"
        elif player_location in all_locations["Loot"]:
            return "loot"
        elif player_location in self.quest_location:
            return "quest"
        else:
            print("Nothing to see here!")
            return "clear"
    
map1 = Map(None)

#map1.get_locations(3, "Enemy")
#map1.get_locations(3, "Merchant")
