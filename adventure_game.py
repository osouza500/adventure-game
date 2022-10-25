import time
import random

def print_pause(message):
    print(message)
    time.sleep(0)

def play_game():
    items = ["horse"]
    intro(items)
    main_street(items)    

def intro(items):
    if "horse" not in items and "gun" in items:
        items.append("horse")
        items.remove("gun")   
    print_pause("You arrive at the main street of the old mining town.")
    print_pause("The sun is setting down.")
    print_pause("Your horse looks tired from the three-day journey "
                "through the desert.")
    main_street(items)

def continue_quit():
    print_pause("Would you like to play again?")
    print_pause("\nEnter 1 if you want to play again.")
    print_pause("Enter 2 if you want to quit.")
    print("What will you do?")
    response = input("(Please enter 1 or 2.)\n")
    if response == "1":
        intro()
    elif response == "2":
        print_pause("Good bye!")
    else:
        print_pause("Please enter a valid number.")
        continue_quit()

def main_street(items):
    print_pause("You are in the main street.")
    print_pause("You look around and see some buildings: a "
                "stable, a saloon and a gun shop.") 
    print_pause("\nEnter 1 to walk to the stable.")
    print_pause("Enter 2 to walk to the saloon.")
    print_pause("Enter 3 to walk to the gunshop.")
    print("What will you do?")
    response = input("(Please enter 1, 2 or 3.)\n")
    if response == "1":
        print_pause("You enter the stable.")
        stable(items)
    elif response == "2" and "horse" in items:
        print_pause("You can't enter the saloon while riding "
                    "a horse.")
        print_pause("You turn around and go back to the main "
                    "street.")
        main_street(items)            
    elif response == "2" and "horse" not in items:
        print_pause("You enter the saloon")
        saloon(items)       
    elif response == "3" and "horse" in items:
        print_pause("You can't enter the gunshop while "
                    "riding a horse.")
        print_pause("You turn around and go back to the main "
                    "street.")
        main_street(items)            
    elif response == "3" and "horse" not in items:
        print_pause("You enter the gunshop.")
        gunshop(items)
    else:
        print_pause("Please enter a valid number")
        main_street(items)       

def stable(items):
    if "horse" not in items:
        print_pause("Your horse is already here.")
        print_pause("You turn around and go back to the main street.")
        main_street(items)
    else:   
        print_pause("The horse groom scowl at you. The service will "
                    "cost you 1 silver dollar.")
        print_pause("\nEnter 1 to pay the man.")
        print_pause("Enter 2 to leave.")
        print("What will you do?")
        response = input("(Please enter 1 or 2.)\n")
        if response == "1":
            print_pause("You pay the man and leave the stable. "
                        "The horse groom will take care of your "
                        "stallion.")
            items.remove("horse")            
            main_street(items)                         
        elif response == "2":
            print_pause("You leave the stable thinking about your avarice.")
            main_street(items)
        else:
            print_pause("Please enter a valid number.")
            stable(items)

def gunshop(items):
    if "gun" in items:
        print_pause("You already have a gun.")
        print_pause("You turn around and go back to the "
                    "main street.")
        main_street(items)            
    print_pause("The clerk at the counter welcomes you.")
    print_pause("He shows you a beautiful gun.")
    print_pause("It costs 1 silver dollar. Do you want "
                "to buy it?")
    print_pause("\nEnter 1 for yes.")
    print_pause("Enter 2 for no.")
    print("What will you do?")
    response = input("(Please enter 1 or 2.)\n")
    if response == "1":
        print_pause("You pay the clerk, take the gun and leave.")
        items.append("gun")
        main_street(items)
    elif response == "2":
        print_pause("You leave the gunshop thinking about your "
                    "avarice.")  
        main_street(items)              
    else:
        print_pause("Please enter a valid number.")
        gunshop(items)

def saloon(items):
    duel_result = ["win", "lose"]
    if "gun" not in items:
        print_pause("The bouncer looks at you and tells you "
                    "that you need a gun in order to access the "
                    "saloon.")
        print_pause("Have you lost your mind?")
        main_street(items)            
    elif "gun" in items:
        print_pause("The place is crowded with crooks.")
        print_pause("One of them challenges you to a duel.")
        print_pause("\nEnter 1 to accept.")
        print_pause("Enter 2 to decline.")
        print("What will you do?")
        response = input("(Please enter 1 or 2.)\n")
        if response == "1" and random.choice(duel_result) == "win":
            print_pause("Your draw your gun...")
            print_pause("...")
            print_pause("... and quickly shot the man dead.")
            print_pause("Congratulations... you won the game!")
            continue_quit()
        elif response == "1" and random.choice(duel_result) == "lose":
            print_pause("Your draw your gun...")
            print_pause("...")
            print_pause("... but you can't do it in time.")
            print_pause("You are dead. Game over!")
            continue_quit()
        elif response == "2":
            print_pause("The crook laughs at you.")
            print_pause("You leave the saloon demoralized.")
            main_street(items)
        else:
            print_pause("Please enter a valid number.")
            saloon(items)                    
                    
play_game()
