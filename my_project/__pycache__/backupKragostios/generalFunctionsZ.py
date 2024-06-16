from printSlowlyFunctionZ import *

def choice_int_checker(min, max):
    choice = input("Choose!")
    while True:
            if isinstance(choice, int):
                if min < choice <= max:
                    return choice
                choice = input("Error! Select a viable option!")
            else: 
                try:
                    choice = int(choice)
                except ValueError:
                    choice = input("Error! Select a viable option!")


def is_vowel(char):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return (char.lower() in vowels)

def option_print_iter(option_presenter: str, option_list: tuple, option_number: int):
    sloprint(option_presenter)
    x = 0
    while x < option_number:
        current_option = option_list[x]
        sloprint(f"Press {x + 1}: to {current_option}.")
        x+=1
    min = 0
    max = option_number
    choice = choice_int_checker(min, max)
    return choice


def noun_print_iter(option_presenter: str, option_list: list, option_number: int):
    sloprint(option_presenter)
    x = 0
    while x < option_number:
        current_option = option_list[x]
        sloprint(f"Press {x + 1}: {current_option}.")
        x+=1
    min = 0
    max = option_number
    choice = choice_int_checker(min, max)
    return choice

#option_print_iter("WHat will you do next?", ("sit", "stand"), 2)