
from lab8.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    old_car = UnreliableCar("Old BMW", 100, 20)

    print("Before driving, ", old_car)
    expected_milage = 40
    actual_milage = old_car.drive(expected_milage)
    if actual_milage == expected_milage:
        print("It has reached the destination.")
    else:
        print("It can not reach the destination.")
    print("After driving, ", old_car)


main()
