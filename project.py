class Vehicle:
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    def displaydetails(self):
        print("Car Details:\n")
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}")
        
class Car(Vehicle):
    def __init__(self,numberOfDoors):
        super().__init__(Make,Model,Year)
        self.numberOfDoors = numberOfDoors 
        
    def displayCarDetails(self):
        print("numberOfDoors:",self.numberOfDoors)
        
class Truck(Vehicle):
    def __init__(self,loadCapacity):
        super().__init__(Make,Model,Year)
        self.loadCapacity = loadCapacity
        
    def displayTruckDetails(self):
        print(f"loadCapacity:,{self.loadCapacity} tons")
        
class Main:
    @staticmethod
    def main():
        make = input()
        model = input()
        year= int(input())
        numberOfDoors = int(input())
        loadCapacity = input()
        
        car = Car(make,make,model,year,numberOfDoors)
        car.displaydetails()
        car.displayCarDetails()
        
        truck = Truck(make,make,model,year,loadCapacity)
        truck.displaydetails()
        truck.displayTruckDetails()
    
        
        
        
Main.main()