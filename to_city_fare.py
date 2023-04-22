import read_reservation

fare_dict_to = {"hosur": 75, "vaniyambadi": 250, "vellore": 500, "walaja": 600, "chennai": 750}
to_city = input("to: ")
regular_seats_available = 12 - read_reservation.seats_booked_regular
tatkal_seats_availabe = 3 - read_reservation.seats_booked_tatkal
fare = fare_dict_to[to_city]
category = input("category(regular or tatkal): ")
if category == "regular":
    seats_available = regular_seats_available
    print("seats available =", seats_available)
    fare = fare

if category == "tatkal":
    seats_available = tatkal_seats_availabe
    print("seats availabe =", tatkal_seats_availabe)
    fare += 100
