from .item_armor import*
from .item_weapon import *
from .item_equipable import *
from .item_usable import *
from .item import ItemType, ItemRarity
from .wornEffects import *
from .debuffsClass import *
from .buffsClass import *
from . import myEnums
class ItemStorage:
        common_items_dict = {}
        rare_items_dict = {}
        epic_items_dict = {}
        legendary_items_dict = {}

        weapon1 = Weapon(name = "simple iron sword", itemType = ItemType.WEAPON, slot = myEnums.SlotType.RIGHT_HAND,
                         value = 5, rarity = ItemRarity.COMMON, damage = 1, weaponType = WeaponType.SWORD, listWornEffects = [])
        weapon1.setWornList([increase_health10]) 

        weapon2 = Weapon(name = "wrist spike", itemType = ItemType.WEAPON, slot= myEnums.SlotType.RIGHT_HAND,
                         value = 5, rarity = ItemRarity.COMMON, damage = 1, weaponType = WeaponType.SWORD)        
        weapon3 = Weapon(name = "iron great axe", itemType = ItemType.WEAPON, slot= myEnums.SlotType.TWO_HAND,
                         value = 5, rarity = ItemRarity.COMMON, damage = 2, weaponType = WeaponType.AXE)
        
        armor1 = Armor(name = "simple iron gloves", slot= myEnums.SlotType.HANDS, itemType= ItemType.ARMOR,
                            value = 5, rarity = ItemRarity.COMMON, armorValue= 1, armorType= ArmorType.IRON)
        armor2 = Armor(name = "simple iron boots", slot= myEnums.SlotType.FEET, itemType= ItemType.ARMOR,
                            value = 5, rarity = ItemRarity.COMMON, armorValue= 1, armorType= ArmorType.IRON)
        armor3 = Armor(name = "simple iron leg gaurds", slot= myEnums.SlotType.LEGS, itemType= ItemType.ARMOR,
                            value = 5, rarity = ItemRarity.COMMON, armorValue= 2, armorType= ArmorType.IRON)
        armor4 = Armor(name = "simple iron chest armor", slot= myEnums.SlotType.CHEST, itemType= ItemType.ARMOR,
                            value = 5, rarity = ItemRarity.COMMON, armorValue= 2, armorType= ArmorType.IRON)
        armor5 = Armor(name = "simple iron helmet", slot= myEnums.SlotType.HEAD, itemType= ItemType.ARMOR,
                            value = 5, rarity = ItemRarity.COMMON, armorValue= 2, armorType= ArmorType.IRON)
        
        new_items = {
        weapon1.name: weapon1,
        weapon2.name: weapon2,
        weapon3.name: weapon3,
        armor1.name: armor1,
        armor2.name: armor2,
        armor3.name: armor3,
        armor4.name: armor4,
        armor5.name: armor5,
        }

        common_items_dict.update(new_items)

        @staticmethod
        def getWeaponInfo(self : Weapon) -> dict:
            weaponObject = ItemStorage.common_items_dict[self.name]
            weaponInfo = {
                "Weapon Description" : weaponObject.name,
                "Slot" : weaponObject.slot,
                "Sale Price" : weaponObject.value,
                "Item Rarity" : weaponObject.rarity,
                "Damage" : weaponObject.damage,
                "Weapon type" : weaponObject.weaponType,
                "Weapon Effects" : weaponObject.listOnHitEffects
            }
            return weaponInfo
        
        @staticmethod
        def getArmorInfo(self : Armor) -> dict:
            armorObject = ItemStorage.common_items_dict[self.name]
            armorInfo = {
            "Armor Description" : armorObject.name,
            "Slot" : armorObject.myEnums.SlotType.slot,
            "Sale Price" : armorObject.value,
            "Item Rarity" : armorObject.rarity,
            "Armor Value" : armorObject.armorValue,
            "Armor Time" : armorObject.armorType,
            "Armor Effects" : armorObject.listOnHitEffects
            }
            return armorInfo
        
 