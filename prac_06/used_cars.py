"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    limo = Car("Limo", 100)     # Create a new Car object called "limo" that is initialised with 100 units of fuel
    limo.add_fuel(20)   # Add 20 more units of fuel to the Limo
    print(f'Limo has fuel: {limo.fuel}')  # Print the amount of fuel in the Limo
    #Attempt to drive the limo 115 km
    distance_driven = limo.drive(115)
    print(f'Limo drove {distance_driven} km')
    #Print the remaining fuel in the Limo
    print(f'Limo has fuel after driving: {limo.fuel}')

    #Print the details of both cars using the __str_- method
    print(my_car)
    print(limo)



main()