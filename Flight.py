from abc import ABC, abstractmethod


# Absztrakt osztály létrehozása

class Flight(ABC):
    def __init__(self, flight_number, destination, price, flight_date):
        self._flight_number = flight_number
        self._destination = destination
        self._price = price
        self._flight_date = flight_date

    @property
    def flight_number(self): return self._flight_number

    @property
    def destination(self): return self._destination

    @property
    def price(self): return self._price
    
    @property
    def date(self): return self._flight_date