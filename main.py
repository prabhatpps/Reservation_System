credentials_read = open("credentials.txt", "r")
ID_Password = credentials_read.readlines()
user_id_input = input("ID: ") + "\n"
password_input = input("Password: ") + "\n"
if user_id_input == ID_Password[0] and password_input == ID_Password[1]:

    reservation_details_append = open("reservation.txt", "a")
    menu_options = input("booking, cancellation, exit : ")
    if menu_options == "booking":
        from_city = input("from: ")
        if from_city == "bangalore":
            import to_city_fare

            import write_reservation

        reservation_details_read = open("reservation.txt", "r")
        if len(reservation_details_read.read()) == 0:
            reservation_details_append.write(write_reservation.total_passengers_details)
        else:
            reservation_details_append.write("-" + write_reservation.total_passengers_details)
    if menu_options == "cancellation":
        import Cancelation
