import time
import random

bag = []

def print_pause(message):
    print(message)
    time.sleep(2)

def stable():
    print_pause("The horse groom scowl at you. The service will "
                "cost you 1 silver dollar.")
    print_pause("You open your bag and see exactly 1 silver dollar.")
    print_pause("Enter 1 to pay the man.")
    print_pause("Enter 2 to bargain with him.")
    response = print_pause(input("What you will do?\n"))
    if response == "1":
        print_pause("You pay the man and leave the stable. "
                    "The horse groom will take care of your "
                    "stallion.")
    elif response == "2":
        print_pause("")
          
stable()