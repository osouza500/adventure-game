import time
import random

bag = ["horse"]

def print_pause(message):
    print(message)
    time.sleep(1)

def intro():
    print_pause("You arrive at the main street of the old mining town.")
    print_pause("The sun is setting down. Your horse looks "
                "tired after the three-day journey through the desert.")
    print_pause("You look around and see some buildings: a stable, "
                "a saloon and a gun shop.")
    main_street()

def main_street():
    while True: 
        print_pause("Enter 1 to walk to the stable.")
        print_pause("Enter 2 to walk to the saloon.")
        print_pause("Enter 3 to walk to the gunshop.")
        response = input("What will you do?\n")
        if response == "1":
            print_pause("You walk to the stable.")
            stable()
        elif response == "2" and "horse" in bag:
            print_pause("You can't enter the saloon riding a horse. ")
        elif response == "2" and "horse" not in bag:
                print_pause("You walk to the saloon")       
        elif response == "3":
            print_pause("You can't enter the gunshop riding a horse. ")    

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
            bag.remove("horse")            
            main_street()            
        elif response == "2":
            print_pause("The horse groom feels offended by your proposal. ")
            print_pause("Enter 1 to fight him.")
            print_pause("Enter 2 to run for your life.")
            response = input("What you will do?\n")
            if response == "1":
                result = random.choice(fight_result)
                if result == "Win":
                    print_pause("You beat the man's arse and leave.")
                    main_street()
                elif result == "Lose":
                    print_pause("Your ass was beaten. Game over")
                    print_pause("Would you like to play again?")
        else:
            print_pause("Please enter a valid number.")       

intro()
main_street()
