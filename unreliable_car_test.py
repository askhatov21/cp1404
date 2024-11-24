from unreliable_car import UnreliableCar

def main():
    car = UnreliableCar("Test Car", 100, 50)
    for i in range(1, 11):
        distance = car.drive(10)
        print(f"Attempt {i}: Drove {distance}km. {car}")

main()
