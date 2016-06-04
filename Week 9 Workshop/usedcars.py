from car import Car

def main():
    bus = Car(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

main()