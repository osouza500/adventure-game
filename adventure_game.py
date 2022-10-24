import time
import random

bag = []

def print_pause(message):
    print(message)
    time.sleep(1)

    

def stable():
    fight_result = ["Win", "Lose"]
    print_pause("The horse groom scowl at you. The service will "
                "cost you 1 silver dollar.")
    print_pause("You open bag and see exactly 1 silver dollar.")
    print_pause("Enter 1 to pay the man.")
    print_pause("Enter 2 to bargain with him.")
    response = input("What you will do?\n")
    if response == "1":
        print_pause("You pay the man and leave the stable. "
                    "The horse groom will take care of your "
                    "stallion.")
    elif response == "2":
        print_pause("The man's face turns red as he stand up and "
                    "jump over you.")
        print_pause("Enter 1 to fight him.")
        print_pause("Enter 2 to run for your life.")
        response = input("What you will do?\n")
        if response == "1":
            result = random.choice(fight_result)
            if result == "Win":
                print("You beat the man's arse and leave.")
                # main_street()
            elif result == "Lose":
                print("Your ass was beaten. Game over")

stable()