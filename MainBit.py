from ClassCustomer import Customer 
from ClassRentalshop import RentalShop
from ClassCustomer import VIPCustomer

car_inventory = {"hatchback": {"standard_price": 30, "discounted_price": 25, # Nested dictionairy containing available cars and prices
                                        "availability": 4},
                            "sedan": {"standard_price": 50, "discounted_price": 40, 
                                      "availability": 3},
                            "SUV":{"standard_price": 100, "discounted_price": 90,
                                   "availability": 3},}     

rental_shop = RentalShop(inventory = car_inventory, rental_records = {})
customer_records = {}  # Empty 

while True:
        print("Welcome to the Loughborough Car Rental shop!")                      # Greetings
        customer_name = input("Please enter your name: ").strip().lower()          # Remove extra spaces from input and lowercase the name
        if customer_name in customer_records:                                      # Existing customers
            customer = customer_records[customer_name]                             #  For record lookup
            print(f"Welcome back, {customer_name.title()}!")
        else: 
            is_vip = input("Are you a VIP customer? (yes/no): ").strip().lower() == "yes"                                    # Ask if customer is a VIP
            if is_vip:                                                                                                       # VIP customer type
                customer = VIPCustomer(customer = customer_name, current_rental = {}, rental_history = [])                   # Original name
                print(f"Welcome, VIP customer {customer_name.title()}!")    
                customer_records[customer_name.lower()] = customer                                                           # Store name lowercase
            else:
                customer = Customer(customer = customer_name, current_rental = {}, rental_history = [])                      # Create regular customer
                print(f"Welcome, {customer_name.title()}!")
                customer_records[customer_name.lower()] = customer                                                           # Store name lowercase


        while True: # Displays menu
    
            print("\nWe have the following options:")
            print("1 View the available cars")
            print("2 Rent a car")
            print("3 Return car")
            print("4 Exit Rental platform")

            print("\n")
            choice = input("Enter your choice: ")

            if choice == "1":            # Option to view available cars
                print("\nOption to view available cars:\n")
                rental_shop.display_inventory()
                print("\n")
            
            elif choice == "2":                     # Option to rent car
                print("\nRenting a car:\n")
                car_type = input("Enter the type of car you want to rent (hatchback, sedan, SUV): ")
                days = int(input("Enter the number of days you want to rent the car: "))
                customer.rent_car(rental_shop, car_type, days)
                print("\n")
            
            elif choice == "3":                    # Option to return a car
                customer.return_car(rental_shop)
                print("\n")
            
            
            elif choice == "4":                    # Option to exit
                print(f"\nThank you for using the car rental platform, {customer_name}!\n")
            
                break                # Loop back to the main menu