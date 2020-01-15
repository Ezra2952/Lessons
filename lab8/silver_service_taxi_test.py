from lab8.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi= SilverServiceTaxi("Hummer", 200, 2)
    print(silver_taxi)
    expected_milage = 18
    silver_taxi.drive(expected_milage)
    print(silver_taxi)

    print("The trip costs: ${:.2f}".format(silver_taxi.get_fare()))


if __name__ == '__main__':
    main()
