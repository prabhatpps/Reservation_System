import copy
import to_city_fare

number_of_passengers = int(input("number of passengers: "))
if number_of_passengers <= to_city_fare.seats_available:
    total_passengers_details = ""
    fare_per_person = copy.deepcopy(to_city_fare.fare)
    passenger_name = input("passenger name: ")
    passenger_age = int(input("passenger age: "))
    if passenger_age >= 60:
        fare_per_person -= fare_per_person / 10
    one_passenger_details = passenger_name + "_" + str(passenger_age) + "_" + to_city_fare.category + "_" + str(
        fare_per_person)
    total_passengers_details += one_passenger_details
    for i in range(number_of_passengers - 1):
        fare_per_person = copy.deepcopy(to_city_fare.fare)
        passenger_name = input("passenger name: ")
        passenger_age = int(input("passenger age: "))
        if passenger_age >= 60:
            fare_per_person -= fare_per_person / 10
        one_passenger_details = passenger_name + "_" + str(passenger_age) + "_" + to_city_fare.category + "_" + str(
            fare_per_person)
        total_passengers_details += "-" + one_passenger_details
else:
    print(number_of_passengers, "seats not available")
