
from goblin import Goblin

import random

import time 

# A grots life. 




              
def main():
    
    gob_name = input("What is your name, you filthy Grot?: ")
    print(gob_name,".. it suits you. Now, go do what grots do..")
    time.sleep(2)
    print( "KILL !!, EAT!!, SLEEP!! AND GET SHINIES !!  ")
    time.sleep(2)
    print("Also maybe get a roof over your head for those rainy days")
    time.sleep(2)      
    gob = Goblin(gob_name,0,100,0,20)

    endgame= False
    choice = None  
    while choice != "0":
        print("")
        print (  "  So... "  ,gob_name, " What is your action ?" )
        print \
        ("""
    
        0 - Quit
        1 - status
        2 - Eat
        3 - Scavenge 
        4 - Explore
        5 - Rest
        6 - Craft 
        """)
    
        choice = input("Choice: ")
        print()

    
        if choice == "0":
            print("Good-bye.")


        elif choice == "1":
            gob.status()
        

        elif choice == "2":
            gob.eat()

        elif choice == "3":
            gob.farm()

        elif choice == "4":
            gob.hunt()

        elif choice == "5":
            gob.rest()

        elif choice == "6":
            gob.craft()
            
        else:

            print("\nSorry, but", choice, "isn't a valid choice.")

        if gob.hunger >20:
            print("died from hunger")
            input("press any button to continue")
            break

        if gob.health <=0:
            print("died from wounds")
            input("press any button to continue")
            break

        if endgame == False:
            if ("Fish Bone Spear") in gob.goal and ("Straw Bed")in gob.goal and("Small Hut") in gob.goal:
                print("You have built your home and prove you are a survivor, you win !!")
                con=input("Do you want to continue playing 1-yes, 2-no" )
                if con == "1":
                    endgame = True

                elif con == "2":
                    print("Good bye")
                    break

                else:
                    pass

            else:
                pass
 
        else:
            pass 




main()
("\n\nPress the enter key to exit.") 
