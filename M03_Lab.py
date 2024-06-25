# Author: Oladayo David Ayorinde
# File name: M03_Lab.py
# Description: This program has two classes, with their appropriate attributes. Then it asks the user to input the vehicle type and then basic information about the vehicle. Then it outputs the data in an easy-to-read and understandable format.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def main():
    vehicle_type = input("Enter the Vehicle type: ")
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Does the car have 2 doors or 4 doors: ")
    roof = input("Enter the type of the roof (solid or sun roof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    print("\nHere are the details of the car you entered: ")
    car.display_info()

if __name__ == "__main__":
    main()


