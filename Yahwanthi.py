
# Assignment 2

# Input
inventory = [55, 92, 18]
user_choice = 0

# Function/Program
def header():
    print("Stock Inventory Management")
    print("*************************")
    print("Inventory")
    print("Soda=", inventory[0])
    print("Chips=", inventory[1])
    print("Hotdogs=", inventory[2])
def add():
    print("\n What inventory would like modify?(Add)\n1) Soda\n2) Chips\n3 Hot Dogs")
def remove():
    print("\n What inventory would like modify?(Remove)\n1) Soda\n2) Chips\n3) Hot Dogs")
def exitprogram():
    exit()

# Output/Program

while True:
    header()
    user_choice = input("1) Add Inventory\n2) Remove Inventory\n3) Exit\nEnter your Selection: ") 
    if user_choice == "1":
        add()
        user_choice = input("Enter your Choice:"  )
        if user_choice == "1":
            user_choice = input("How much Soda would you like to add to the inventory?: ")
            inventory[0] = int(inventory[0]) + int(user_choice)
            if inventory[0] > 100:
                    print("Please enter a number less then 100!\n")
                    inventory[0] = int(inventory[0]) - int(user_choice)
        elif user_choice == "2":
            user_choice = input("How many Chips would you like to add to the inventory?: ")
            inventory[1] = int(inventory[1]) + int(user_choice)
            if inventory[1] > 100:
                    print("Please enter a number less then 100!\n")
                    inventory[1] = int(inventory[1]) - int(user_choice)
        elif user_choice == "3":
            user_choice = input("How many hotdogs would you like to add to the inventory?:   ")
            inventory[2] = int(inventory[2]) + int(user_choice)
            if inventory[2] > 100:
                   print("Please enter a number less then 100!\n")
                   inventory[3] = int(inventory[2]) - int(user_choice)
    elif user_choice == "2":
        remove()
        user_choice = input("Enter your Choice"  )
        if user_choice == "1":
            user_choice = input("How much soda would you like to remove from the inventory?:  ")
            inventory[0] = int(inventory[0]) - int(user_choice)
            if inventory[0] < 0:
                print("We do not have enough of that product!\n")
                inventory[0] = int(inventory[0]) + int(user_choice)
            elif user_choice == "2":
                    user_choice = input("How many chips would you like to remove from the inventory?:  ")
                    inventory[1] = int(inventory[1]) - int(user_choice)
                    if inventory[1] < 0:
                        print("We do not have enough of that product!\n")
                        inventory[1] = int(inventory[1]) + int(user_choice)
                    elif user_choice == "3":
                            user_choice = input("How many hotdogs would you like to remove?:   ")
                            inventory[2] = int(inventory[2]) - int(user_choice)
                            if inventory[2] < 0:
                                print("We do not have enough of that product!\n")
                                inventory[2] = int(inventory[2]) + int(user_choice)
                            else:
                                    print("Your choice doesn't exist.")
                    else:
                            exitprogram()
                
         
    
               
            
                               
            
