class Vehicle:
    def __init__(self,newName):
        self.name = newName
        self.wheels = 0
        self.ignition = False
        self.passengers = []

def num_wheels(self,newWheels):
    self.wheels = newWheels

def ignition(self, key):
    self.ignition = key

def add_passenger(self, newPassenger):
    self.passengers.append(newPassenger)

def main():
    myCar = Vehicle("Corolla")
    myCar.num_wheels(4)
    myCar.add_passenger("Kemi")
    print(myCar.name, myCar.wheels, myCar.passengers)

if __name__ == '__main__':
    main()
