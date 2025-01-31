# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels: int = 4):
        self.num_wheels = num_wheels
        
    def drive(self):
        message = 'vroooom'
        return(message)
        

    

# Subclass Motorcycle from GroundVehicle.
#
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels: int = 2):
        self.num_wheels = num_wheels
    def drive(self):
        message = 'BRAAAP!!'
        return(message)
        

# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]


for i in vehicles:
    a = i
    print(i.drive())