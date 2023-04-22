reservation_details_read = open("reservation.txt", "r")
data_stored_per_person_0 = reservation_details_read.read().split("-")
while "" in data_stored_per_person_0:
    data_stored_per_person_0.remove("")
data_stored_per_person = []
seats_booked_regular = 0
seats_booked_tatkal = 0
if ""not in data_stored_per_person_0:
    for i in data_stored_per_person_0:
        data_stored_per_person.append(i.split("_"))
    if len(data_stored_per_person) != 0:
        for i in range(len(data_stored_per_person)):
            if data_stored_per_person[i][2] == "regular":
                seats_booked_regular += 1
            if data_stored_per_person[i][2] == "tatkal":
                seats_booked_tatkal += 1
