# Enter your code here. Read input from STDIN. Print output to STDOUT

class Car:
    def __init__(self,brand,model,year,price,engineCapacity):
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price
        self.engineCapacity=engineCapacity
    
    
    def DisplayDetails(self):
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: ${self.price}")
        print(f"Engine Capacity: {self.engineCapacity} L")
        
class Main:
    @staticmethod
    def main():
        brand=input()
        model=input()
        year=int(input())
        price=float(input())
        engineCapacity=float(input())

        if year <=1885 or price<=0 or engineCapacity<=0:
            print("Invalid Input")
        else:
            car1=Car(brand,model,year,price,engineCapacity)
            car1.DisplayDetails()
Main.main()