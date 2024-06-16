import time
import sys
slow = False
def sloprint(text):
    if slow == True:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()  # Ensure the character is immediately displayed
            time.sleep(.05)
        print(" ", end = '\n')
    else:
        print(text)
    

def supersloprint(text):
    if slow == True:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()  # Ensure the character is immediately displayed
            time.sleep(.2)
        print(" ", end = '\n')
    else:
        print(text)
    
def slow_think():
    text = f"..... \n ....."
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensure the character is immediately displayed
        time.sleep(.4)
    print(" ", end = '\n')
