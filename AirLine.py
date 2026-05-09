
class AirLine:
    def __init__(self, name):
        self.name = name
        self.flights = []

    
    def add_flight(self, flight):
        self.flights.append(flight)
        