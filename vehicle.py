# make parent class
class Vehicle:
    def __init__(self, chasis_number, vehicle_brand, ex_showroom_price, **kwargs):
        self.chasis_number = chasis_number
        self.vehicle_brand = vehicle_brand
        self.ex_showroom_price = ex_showroom_price
        self.additonal_features = kwargs
        
    def get_details(self):
        return {
            "chasis number": self.chasis_number,
            "vehicle brand": self.vehicle_brand,
            "ex-showroom price": self.ex_showroom_price,
            **self.additonal_features    
        }
        
class Car(Vehicle):
    def __init__(self, chasis_number, vehicle_brand, ex_showroom_price, category, **kwargs):
        super().__init__(chasis_number, vehicle_brand, ex_showroom_price, **kwargs)
        self.category = category
        
class Bike(Vehicle):
    def __init__(self, chasis_number, vehicle_brand, ex_showroom_price, category, **kwargs):
        super().__init__(chasis_number, vehicle_brand, ex_showroom_price, **kwargs)
        self.category = category
        
class Inventory:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        
    def get_vehicle_by_chasis_number(self, chasisNumber):
        for vehicle in self.vehicles:
            if vehicle.chasis_number == chasisNumber:
                return vehicle.get_details()
        return None
    def vehicle_count(self, category):
        count = 0
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car):
                if vehicle.category == category:
                    count += 1
            elif isinstance(vehicle, Bike):
                if vehicle.category == category:
                    count += 1
        return count
    
    def average_price(self, category):
        count = 0
        total_price = 0
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car):
                if vehicle.category == category:
                    count += 1
                    total_price += vehicle.ex_showroom_price
            elif isinstance(vehicle, Bike):
                if vehicle.category == category:
                    count += 1
                    total_price += vehicle.ex_showroom_price
        return total_price/count if count > 0 else 0
    
if __name__=="__main__":
    
    #taking some of the examples:
    inventory = Inventory()
    # adding vehicles details:
    car1 = Car("CR12", "TESLA", 800000, "SUV", total_seats=6, insurance_amount=5000)
    car2 = Car("CR15", "TATA", 600000, "HatchBack", total_seats=8, insurance_amount=3000)
    bike1 = Bike("BK11", "HERO", 100000, "Commute", insurance_amount=1000)
    bike2 = Bike("BK16", "BAJAJ", 100000, "Sports", insurance_amount=1000)
    
    # to add the vehicle in the inventory:
    inventory.add_vehicle(car1)
    inventory.add_vehicle(car2)
    inventory.add_vehicle(bike1)
    inventory.add_vehicle(bike2)

    # to get the vehicle by chasis number:
    print("Deatails of the vehicle with the chasis number: CR15")
    print(inventory.get_vehicle_by_chasis_number("CR15"))
    
    # to get the count of vehicle of specific category:
    print(f"Total number of commute bikes are {inventory.vehicle_count("Commute")}")
    
    # to get the average price of vehicle of specific category:
    print(f"Average price of the HatchBack car is {inventory.average_price("HatchBack")}")
    
    
        
        
                        
        
                
        

        
        

    
