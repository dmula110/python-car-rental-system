class Customer:
    """Definition of Customers class """
    def __init__(self, customer, current_rental , rental_history ): # Customer attributes
        
        self.customer = customer                                     # Name of customer
        self.current_rental = current_rental  # Details of the current car rental
        self.rental_history = rental_history  # List to track previous rentals by the customer
   
    def browse_stock(self,rental_shop):  # Customer view car availbility and prices in shop   
        rental_shop.display_inventory()  # Show available cars and prices to the customer

    def rent_car(self,rental_shop, car_type,days):                    # Rent car method  
     if rental_shop.inventory[car_type]["availability"] > 0:          # If the requested car type is available
        rental_shop.process_rental_request(self.customer, car_type, days) # Process the rental request through the RentalShop's method
        if days < 7: 
          cost_per_day = rental_shop.inventory[car_type]["standard_price"] # Standard price for rental less than 7 days
        else: 
         cost_per_day = rental_shop.inventory[car_type]["discounted_price"]              # Discounted price for 7 day+ 
        total_cost = cost_per_day * days
        self.current_rental = { "car_type": car_type,"days": days,"cost": total_cost} 
        print(f"You have rented a {car_type} for {days} days at £{cost_per_day} per day. Total cost: £{total_cost}.") # Customer has rented car
     else:
         print(f"Sorry, {car_type} is not available at the moment.")  # Car is out of stock

    def return_car(self,rental_shop):
        if self.current_rental:                           # Check if the customer has an active rental
         car_type = self.current_rental["car_type"]       # Car type from the current rental information
         rental_shop.update_stock(car_type, "return")     # Update the inventory in the rental shop 
         rental_shop.issue_bill(self.customer)            # Issue the bill for the completed rental
         self.rental_history.append(self.current_rental)  # Add the current rental details to the customer's rental history
         self.current_rental = {}                         # Clear the current rental information
        else:
         print("You do not have any car to return")


class VIPCustomer(Customer):
    """VIP Customer class inheriting from the Customer class."""
    
    VIP_RATES = { "hatchback": 20, "sedan": 35,"SUV": 80,}

    def __init__(self, customer, current_rental , rental_history):
        super().__init__(customer, current_rental, rental_history)                                     # Initialise parent
        self.is_vip = True                                                                             # Identify VIP customers

    def rent_car(self, rental_shop, car_type, days):                                                   # Rent car method  
        if car_type in rental_shop.inventory and rental_shop.inventory[car_type]["availability"] > 0:  # If the requested car type is available
            rental_shop.process_rental_request(self.customer, car_type, days)
            cost_per_day = self.VIP_RATES[car_type]                                                    # VIP rates cost
            total_cost = cost_per_day * days                                                           # Total cost
            self.current_rental = {"car_type": car_type, "days": days, "cost": total_cost}             # VIP customer purchase 
            print(f"As our loyal VIP customer, you have rented a {car_type} for {days} days at £{cost_per_day} per day." ) # Loyal VIP customer
            print(f"Total cost: £{total_cost}.")
        else:
            print(f"Sorry, {car_type} is not available at the moment.")    

    def return_car(self, rental_shop):
        if self.current_rental:                          # Check active rental
            car_type = self.current_rental["car_type"]   # Get car type
            rental_shop.update_stock(car_type, "return") # Update inventory
            rental = self.current_rental                 # Get rental details
            days = rental["days"]                        # Get rental days
            cost_per_day = self.VIP_RATES[car_type]      # Get VIP rate
            total_cost = cost_per_day * days             # Totl cost
            print(f"As a VIP customer, your rental bill for the {car_type} is:")
            print(f"Days: {days}, Rate: £{cost_per_day}/day, Total: £{total_cost}")

            self.rental_history.append(self.current_rental) # Add to rental history
            self.current_rental = {}                        # Clear current rental
        else:
            print("You do not have any car to return.")