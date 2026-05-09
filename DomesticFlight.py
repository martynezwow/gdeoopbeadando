from Flight import Flight


class DomesticFlight(Flight):
    def __init__(self, flight_number, destination, price, flight_date):
        super().__init__(flight_number, destination, price, flight_date)
        self.type = "Belföldi"