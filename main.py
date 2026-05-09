from AirLine import AirLine
from DomesticFlight import DomesticFlight
from InternationalFlight import InternationalFlight
from TicketBooking import TicketBooking
from datetime import datetime
from Flight import Flight

# Globális tárolók
bookings = []
airline = AirLine("Python AirWayz")

def inicialization():
    f1 = DomesticFlight("D104", "Budaörs", 15000, "2026-05-11")
    f2 = InternationalFlight("I904", "Gran Canaria", 49000, "2026-07-20")
    f3 = InternationalFlight("I723", "Dubai", 170000, "2026-12-10")
    for f in [f1, f2, f3]: airline.add_flight(f)
    names = ["Tamás", "Kinga", "Zoltán", "Martínez", "Dávid", "Xavier"]
    for i in range(6):
        current_flight = airline.flights[i % 3]
        bookings.append(TicketBooking(current_flight, names[i], current_flight._flight_date))

def b_menu():
    print("\n--- Jegyfoglalás ---")
    for i, f in enumerate(airline.flights):
        print(f"{i}. {f.flight_number} - {f.destination} ({f.price} Ft) {f._flight_date}")
    try:
        choice = int(input("Válassz járatot (szám): "))
        selected_flight = airline.flights[choice] 
        
        name = input("Utas neve: ")
        date_str = input("Dátum (YYYY-MM-DD): ")
        
        # 1. Validáció
        datetime.strptime(date_str, "%Y-%m-%d") 
        
        # 2. Validáció
        if date_str != selected_flight._flight_date:
            print(f"Hiba: Ezen a napon nem indul járat! (Jó dátum: {selected_flight._flight_date})")
            return
        
        # 3. Létrehozás
        new_booking = TicketBooking(selected_flight, name, date_str)
        bookings.append(new_booking)
        print("Sikeres foglalás!")
        
    except Exception as e:
        print(f"Rendszerhiba: {e}") 

def remove_menu():
    listing()
    try:
        index = int(input("Törlendő sorszám: "))
        del bookings[index]
        print("Sikeres törlés!")
    except:
        print("Érvénytelen sorszám!")

def listing():
    print("\n--- Aktuális foglalások ---")
    for i, f in enumerate(bookings):
        print(f"{i}. {f.info}")

def main():
    inicialization()
    while True:
        print(f"\n--- {airline.name} Rendszer ---")
        print("1. Jegy foglalás\n2. Foglalás lemondása\n3. Foglalások listázása\n4. Kilépés")
        choose = input("Válasz: ")
        if choose == "1": b_menu()
        elif choose == "2": remove_menu()
        elif choose == "3": listing()
        elif choose == "4": break

if __name__ == "__main__":
    main()
