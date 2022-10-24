import time
import random

bag = []

def print_pause(message):
    print(message)
    time.sleep(1)

def intro():
    print_pause("You arrive at the mains street of the old mining town.")
    print_pause("The sun is setting down. Your horse looks "
                "tired after the three-day journey through the desert.")
    print_pause("You look around and see some buildings: a stable, "
                "a saloon and a gun shop.")
    # main_street()       

def stable():
    fight_result = ["Win", "Lose"]
    while True:
        print_pause("The horse groom scowl at you. The service will "
                    "cost you 1 silver dollar.")
        print_pause("You open your bag and see exactly 1 silver dollar.")
        print_pause("Enter 1 to pay the man.")
        print_pause("Enter 2 to bargain with him.")
        response = input("What you will do?\n")
        if response == "1":
            print_pause("You pay the man and leave the stable. "
                        "The horse groom will take care of your "
                        "stallion.")
            # main_street()            
        elif response == "2":
            print_pause("The horse groom feels offended by your proposal. ")
            print_pause("Enter 1 to fight him.")
            print_pause("Enter 2 to run for your life.")
            response = input("What you will do?\n")
            if response == "1":
                result = random.choice(fight_result)
                if result == "Win":
                    print_pause("You beat the man's arse and leave.")
                    # main_street()
                elif result == "Lose":
                    print_pause("Your ass was beaten. Game over")
                    print_pause("Would you like to play again?")
        else:
            print_pause("Please enter a valid number.")       

stable()