from datetime import datetime
from AirLine import AirLine

class TicketBooking:
    def __init__(self, flight, passenger_name, flight_date):
        self._flight = flight
        self._passenger_name = passenger_name
        self._date = flight_date


    @property
    def info(self):
        return f"Utas: {self._passenger_name}, Járat: {self._flight.flight_number} ({self._flight.destination}), Dátum: {self._date}"


        

