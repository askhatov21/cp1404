from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Limo", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"Fare: ${taxi.get_fare()}")

main()
