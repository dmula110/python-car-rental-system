class RentalShop:
    """Definition of Rental Shop class """
    def __init__(self, inventory, rental_records):         # Rental attributes

        self.inventory = inventory                         # Cars and prices
        self.rental_records = rental_records               # Tracks ongoing rentals between customer and rental shop
    
    def display_inventory (self):  
        total_cars = sum(details['availability']             # Total Car calculation
        for details in self.inventory.values())              # Loop  each car in the inventory
        print(f"Total cars available: {total_cars}")         # Total available cars
        
        for car_type, details in self.inventory.items():
            print(f"{car_type.title()}:") # Car type
            print(f"  Standard Price: £{details['standard_price']} per day\n")                  # Display of standard price
            print(f"  Discounted Price (7+ days): £{details['discounted_price']} per day\n")    # Display discounted price
            print(f"  Available: {details['availability']} cars\n")                             # Displays Car Availability
    
    
    def process_rental_request (self, customer, car_type, days):                        # Check if the requested car type is available
        if car_type in self.inventory and self.inventory[car_type]["availability"] > 0: # heck car availability
            self.update_stock(car_type, "rent")                                         # Use update_stock here
            self.rental_records[customer] = { "car_type": car_type,                     # Rental record
                                  "days": days,}
            print(f"Rental confirmed for {customer} for {days} days.")
            print(f"You have rented a {car_type} for {days} days.")
        else:
           print(f"Sorry, {car_type} is not available at the moment.")    # Car not available

    def issue_bill (self,customer):                                       # issue bill method
        rental = self.rental_records.get(customer)                        # Extract details from the rental record
        if rental: 
            car_type = rental["car_type"]
            days = rental["days"]
        if days < 7:                                                       # Standard price for rental less than 7 days
            cost_per_day = self.inventory[car_type]['standard_price']
        else:
            cost_per_day = self.inventory[car_type]['discounted_price']    # Discounted price for 7 day+ 
        total_cost = cost_per_day * days                                   # Total cost for  Rental period 
       
        print(f"You have rented a {car_type} for {days} days at £{cost_per_day} per day.") # Customer has rented car
        print(f"Total cost: £{total_cost}")                                       # Customer bill
   
   
    def update_stock(self, car_type, action):                     # Update stock method
        if car_type in self.inventory:                            # Check if there is at least one car available
            if action == "rent":
                self.inventory[car_type]["availability"] -= 1     # Updating stock
                print(f"{car_type} rented. Updated availability: {self.inventory[car_type]['availability']}")
                    
            elif action == "return":                          # Increase the availability to reflect a returned car
             self.inventory[car_type]["availability"] += 1    # Update car inventory
             print(f"{car_type} returned. Updated availability: {self.inventory[car_type]['availability']}")
            else:
                print("Invalid action. Please use 'rent' or 'return'.")
        else:
            print(f"{car_type} is not in the inventory.")

