import read_reservation

reservation_details_write = open("reservation.txt", "w")

passenger_name = input("passenger name: ")
passenger_age = int(input("passenger age: "))
for i in read_reservation.data_stored_per_person:
    if read_reservation.data_stored_per_person[i][0] == passenger_name and read_reservation.data_stored_per_person[i][1] == passenger_age:
        read_reservation.data_stored_per_person.remove(i)
    else:
        print("wrong details")
total_passengers_details = ""

for i in range(len(read_reservation.data_stored_per_person)):
    passenger_name = read_reservation.data_stored_per_person[i][0]
    passenger_age = read_reservation.data_stored_per_person[i][1]
    category = read_reservation.data_stored_per_person[i][2]
    fare_per_person = read_reservation.data_stored_per_person[i][3]
    one_passenger_details = passenger_name + "_" + str(passenger_age) + "_" + category + "_" + str(
        fare_per_person)
    total_passengers_details += "-" + one_passenger_details
total_passengers_details = total_passengers_details.replace("-", "", 1)
reservation_details_write.write(total_passengers_details)
