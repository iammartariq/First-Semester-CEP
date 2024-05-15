#importing builtin modules

import getpass #it is use to hide the input of sensitive information, such as passwords, when entered by the user.

import os #The 'os.system()' function is used here to clear the console screen, providing a cleaner output.

import time #time for user history

#defining functions

def clear_console():

    os.system(
        "cls"
        )

def colortext(text, color): #colors for warning messages

    colors = {
        "red": "\033[91m",
        "blue": "\033[94m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "orange": "\033[33m",        
        "magenta":'\033[35m',
        "cyan":'\033[36m',
        "white":'\033[37m',
        "reset": "\033[0m",
                }

    return f"{colors[color]}{text}{colors['reset']}"


def checkout(username):

    total_price = calculate_total_price()
    x = time.localtime()
    shopping_history = {
        "username": f"{username}",
        "date": f"{x.tm_year}-{x.tm_mon}-{x.tm_mday}",
        "time": f"{x.tm_hour}:{x.tm_min}:{x.tm_sec}",
        "items": shopping_cart.copy(),
        "total_bill": total_price,
                        }

    with open("history.txt","a") as file:
        file.write(f"{shopping_history}\n")

    # Clear the cart after checkout
        
    shopping_cart.clear()
    print(colortext
          ("Checkout successful. Items transferred to shopping history.", 
                    "green"
                    )
                    )

def view_history(username):

    with open("history.txt", "r") as history_file:
        print(colortext
              ("Your Shopping History:", 
               "blue"
               )
               )

        for line in history_file:
            history_entry = eval(line.strip())  # Convert the string to a dictionary

            if history_entry["username"] == username:
                print(f"Date: {history_entry['date']}, Time: {history_entry['time']}")
                print("Items:")
                for item, quantity in history_entry["items"].items():
                    print(f"\t{item}: Quantity - {quantity}")
                print(f"Total Bill: Rs{history_entry['total_bill']}")
                print("------------------------")

# Define a dictionary for the menu with prices and quantities
   
menu = {
    "rice": {"price": 400, "quantity": 200},
    "bread": {"price": 120, "quantity": 100},
    "sugar": {"price": 250, "quantity": 200},
    "eggs": {"price": 35, "quantity": 600},
    
    "cold drinks": {"price": 180, "quantity": 200},
    "juices": {"price": 150, "quantity": 200},
    "tea": {"price": 120, "quantity": 200},
    "milk": {"price": 300, "quantity": 400},
    
    "cotton buds": {"price": 100, "quantity": 200},
    "soap": {"price": 60, "quantity": 300},
    "toothpaste": {"price": 200, "quantity": 200},
    "toothbrush": {"price": 90, "quantity": 100},
    
    "tissues": {"price": 220, "quantity": 30},
    "sanitizer": {"price": 100, "quantity": 520},
    "mask": {"price": 8, "quantity": 900},
    "band-aid": {"price": 5, "quantity": 900},
}

newline_positions = [4, 8, 12]

# Function to display the menu

def display_menu():
    i = 0

    print(colortext
          ("<< Menu >>",
                    "blue"
                    )
                    )
    
    for item, details in menu.items():
        print(colortext(f"{item}: Price - Rs{details['price']}, Quantity - {details['quantity']}",
                        "yellow"
        )
        )
        
        i += 1
        if i in newline_positions:
            print()

# Function to update the quantity when a product is added to the cart
        
def update_quantity(item, quantity):

    if item in menu and menu[item]["quantity"] >= quantity:
        menu[item]["quantity"] -= quantity
        print(colortext(f"{quantity} {item}(s) added to the cart.", "green"))

    else:
        print(colortext("Invalid or insufficient quantity.",
                        "red"
                        )
                        )

# Function to add products to the cart
        
def add_to_cart(item, quantity):

    if item in menu and menu[item]["quantity"] >= quantity:

        if item in shopping_cart:
            shopping_cart[item] += quantity

        else:
            shopping_cart[item] = quantity
        menu[item]["quantity"] -= quantity
        print(colortext
              (f"{quantity} {item}(s) added to the cart.", 
               "green"
               )
               )
        display_menu()
        
    else:
        print(colortext
              ("Invalid item or insufficient quantity.", 
               "red"
               )
               )
        
def add_products():

            display_menu()
            while True:
                        
                        item_choice = input("Enter the item you want to add to the cart (or type 'done' to finish): ").lower()

                        if item_choice == 'done':
                            break

                        # Check if the entered item is in the menu

                        if item_choice in menu:

                            try:

                                quantity = int(input
                                            (f"Enter the quantity of {item_choice} you want to add: "
                                                )
                                                )
                                add_to_cart(item_choice, quantity)

                            except ValueError:
                                print(colortext
                                    ("Invalid input. Please enter a valid quantity.", 
                                    "red"
                                    )
                                    )
                        
                        else:
                            print(colortext
                                    ("Invalid input. Please enter a valid item.", 
                                    "red"
                                    )
                                    )

                    # Display the items in the cart
                            
            print(colortext
                ("Items in your cart:", 
                "blue"
                )
                )
            
            for item, quantity in shopping_cart.items():
                print(f"{item}: Quantity - {quantity}")

# Function to calculate the total price of items in the cart
        
def calculate_total_price():

    total_price = 0

    for item, quantity in shopping_cart.items():
        total_price += menu[item]["price"] * quantity

    return total_price

# Initialize shopping cart

shopping_cart = {}

#create account
    
# Name

def make_account():

    while True:

        name = input("Enter your full name: ")

        if any(char.isdigit() for char in name):
            print(colortext
                  ("Name cannot contain a digit",
                   "red"
                   )
                   )
            
        elif name == "":
            print(colortext
                  ("Name is required",
                   "red"
                   )
                   )
            
        else:

            break

    # username

    while True:

        username = input("Enter your username: ")

        if username == "":
            print(colortext
                  ("Username is required",
                   "red"
                   )
                   )
        
        elif not any(char.isdigit() for char in username):
            print(colortext
                  ("Username must contain a digit",
                   "red"
                   )
                   )
            
        else:

            with open('main.txt', 'r') as file:  # Check if the username already exists in the file
                existing_usernames = [eval(line.strip())["username"] for line in file]

                if username in existing_usernames:
                    print(colortext
                          ("Username already exists, please choose a different username.",
                           "red"
                           )
                           )    
                    
                else:
                    print(colortext
                          ("Username succesfully verified",
                           "green"
                           )
                           )
                    
                    break

    # Email

    while True:

        email = input("Enter your email (ending with @gmail.com): ")

        if email.endswith("@gmail.com"):
            print(colortext
                  ("Email succesfully verified",
                   "green"
                   )
                   )
            
            break

        elif email == "":
            print(colortext
                  ("Email is required",
                   "red"
                   )
                   )

        else:
            print(colortext
                  ("Please enter your email ending with '@gmail.com'",
                   "red"
                   )
                   )

    # Password

    while True:

        print(colortext
              ("Enter your password with the following conditions:\n\t1. Minimum 8 characters\n\t2. Must contain a digit",
               "yellow"
              )
              )
        
        password = getpass.getpass("Enter password: ")

        if len(password) < 8:
            print(colortext
                  ("Password must be of atleast 8 characters",
                   "red"
                   )
                   )
            
        elif password == "":
            print(colortext
                  ("Password is required",
                   "red"
                   )
                   )
            
        elif not any(char.isdigit() for char in password):
            print(colortext
                  ("Password must contain a digit",
                   "red"
                   )
                   )
            
        else:
            print(colortext
                  ("Password is valid",
                   "yellow"
                   )
                   )
            
            break

    while True:

        re_enter_password = getpass.getpass("Please re-enter your password: ")

        if re_enter_password != password:
            print(colortext
                  ("Please re-enter a correct password",
                   "red"
                   )
                   )
            
        elif re_enter_password == "":
            print(colortext
                  ("Re-enter password is required",
                   "red"
                   )
                   )

        else:
            print(colortext
                  ("Password successfully verified",
                   "green"
                   )
                   )
            
            break

    # Contact Number

    while True:

        contact = input("Enter your phone number (11 digits): ")

        if len(contact) == 11 and contact.isdigit():
            print(colortext
                ("Contact number successfully verified",
                "green"
                )
                )
            
            break

        elif contact == "":
            print(colortext
                  ("Phone number is required",
                   "red"
                   )
                   )

        else:
            print(colortext
                ("Please enter a correct contact number of 11 digits",
                "red"
                )
                )

    #address

    while True:

        address = input("Enter full address: ")
        if address == "":
            print(colortext
                  ("Address is required",
                   "red"
                   )
                   )
        
        else:
            
            break

    print(colortext
        ("                      <<<ACCOUNT SUCCESSFULLY CREATED>>>",
        "blue"
            )
            )
    
    #create account filing

    user_data = {
    "full name": f"{name}",
    "username": f"{username}",
    "email": f"{email}",
    "password": f"{password}",
    "contact":f"{contact}",
    "address":f"{address}"
                        }
    
    with open('main.txt', 'a') as file:
        file.write(f"{user_data}\n")


#login
        
def login():

    while True:

        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        with open('main.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                user_data = eval(line.strip())

                if user_data["username"] == username and user_data["password"] == password:
                    return username
                
            else:
                print(colortext
                        ("Username or password is incorrect, please try again",
                            "red"
                            )
                            )
                ask = input("Do you want to continue with login or signup? (login/signup): ")

                if ask == "login":
                    login()

                    break
                                        
                elif ask == "signup":
                    make_account()

                    break

                else:
                    print(colortext
                        ("Invalid item. Please choose a valid item from the menu.", 
                            "red"
                            )
                            )



#shopping cart startup page
                
print(colortext
      ("""
                        <<< WELCOME TO SHOPPING CART >>>""",
       "blue"
        )
        )       

while True:

    choice = (input
              (colortext("""
What would you like to do?
                        Type '1' to create an account
                        Type '2' to login into an account
                        Type '3' to exit
            Type here:
            """,
            "magenta"
            )
              )
    )
    clear_console()
    print(colortext
          (f"You entered: {choice}",
           "blue"
          )
          )
    
    if choice == "1":
        print(colortext
              ("Sign up page",
               "yellow"
               )
               )
        
        make_account()
        clear_console

    elif choice == "2":
            print(colortext
            ("Login page",
            "yellow"
            )
            )

            username = login()

            clear_console()
            print(colortext("Successfully logged in", "green"))

            while True:

                cart_option = input(colortext
                                    ("""
                What would you like to do?
                1 - Add products to cart                   
                2 - Show added items
                3 - View total bill
                4 - Remove a product from the cart
                5 - Clear the entire cart
                6 - Checkout
                7-  View history
                8 - Logout
                Enter the corresponding number: 
                                    """,
                                    "magenta"
                                    )
                                    )

                if cart_option == "1":

                    add_products()
                
                elif cart_option == "2":

                    print(colortext
                          ("Items in your cart:", 
                                    "blue"
                                    )
                                    )

                    for item, quantity in shopping_cart.items():

                        print(f"{item}: Quantity - {quantity}")

                elif cart_option == "3":

                    total_price = calculate_total_price()

                    print(colortext
                          (f"Total Bill: Rs{total_price}", 
                                    "green"
                                    )
                                    )

                elif cart_option == "4":
                    item_to_remove = input("Enter the item you want to remove from the cart: ").lower()

                    if item_to_remove in shopping_cart:
                        
                        while True:

                            try:

                                quantity_to_remove = int(input
                                            (f"Enter the quantity you want to remove: "
                                                )
                                                )
                                break

                            except ValueError:
                                print(colortext
                                    ("Invalid input. Please enter a valid quantity.", 
                                    "red"
                                    )
                                    )
                        
                        if quantity_to_remove <= shopping_cart[item_to_remove]:
                            menu[item_to_remove]["quantity"] += quantity_to_remove
                            shopping_cart[item_to_remove] -= quantity_to_remove
                            print(colortext
                                  (f"{quantity_to_remove} {item_to_remove}(s) removed from the cart.", 
                                            "green"
                                            )
                                            )
                            
                        else:
                            print(colortext
                                  ("Invalid quantity. Not enough items in the cart.", 
                                   "red"
                                   )
                                   )
                            
                    else:
                        print(colortext
                              ("Invalid item. The item is not in the cart.", 
                               "red"
                               )
                               )

                elif cart_option == "5":

                    for item, quantity in shopping_cart.items():
                        menu[item]["quantity"] += quantity
                    shopping_cart = {}
                    print(colortext
                          ("Cart cleared.", 
                           "green"
                           )
                           )

                elif cart_option == "6":
                    confirmation = input("Are you sure you want to checkout? (yes/no): ").lower()

                    if confirmation == "yes":

                        for item, quantity in shopping_cart.items():
                            print(colortext
                                  (f"item - {item}: Quantity - {quantity}",
                                   "yellow",
                                  )
                                  )

                        total_price = calculate_total_price()
                        print(colortext
                          (f"Total Bill: Rs{total_price}", 
                                    "green"
                                    )
                                    )
                        checkout(username)

                    else:
                        print(colortext
                              ("Checkout canceled.", 
                               "yellow"
                               )
                               )   

                elif cart_option == "7":
                    view_history(username)  

                elif cart_option == "8":
                    clear_console()
                    print(colortext
                        ("Logged out successfully.",
                        "yellow"
                        )
                        )
                    break


                else:
                    print(colortext
                          ("Invalid option. Please choose a valid option.", 
                           "red"
                           )
                           )
            
    elif choice == "3":        
        clear_console()
        print(colortext
              ("Thank you for using our site!",
               "yellow"
               )
               )
        


        break

    else:
        print(colortext
              ("Invalid choice, please try again",
               "red"
               )
               )
        
        clear_console()
