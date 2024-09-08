# 1. Importujeme knihovnu abc, která umožňuje vytváření abstraktních tříd
from abc import ABC, abstractmethod

# 2. Abstraktní třída pro pozemní dopravu
class LandTransport(ABC):
    @abstractmethod
    def drive(self):
        # Abstraktní metoda, kterou musí implementovat všechny pozemní dopravní prostředky
        pass

# 3. Abstraktní třída pro námořní dopravu
class SeaTransport(ABC):
    @abstractmethod
    def sail(self):
        # Abstraktní metoda, kterou musí implementovat všechny námořní dopravní prostředky
        pass

# 4. Konkrétní třída Car (Auto), která implementuje pozemní dopravu
class Car(LandTransport):
    def drive(self):
        # Implementace metody drive pro auto
        return "Car is driving on the road."

# 5. Konkrétní třída Bike (Kolo), která implementuje pozemní dopravu
class Bike(LandTransport):
    def drive(self):
        # Implementace metody drive pro kolo
        return "Bike is pedaling on the road."

# 6. Konkrétní třída Ship (Loď), která implementuje námořní dopravu
class Ship(SeaTransport):
    def sail(self):
        # Implementace metody sail pro loď
        return "Ship is sailing on the sea."

# 7. Konkrétní třída Submarine (Ponorka), která implementuje námořní dopravu
class Submarine(SeaTransport):
    def sail(self):
        # Implementace metody sail pro ponorku
        return "Submarine is navigating underwater."

# 8. Abstraktní továrna, která definuje metody pro vytváření pozemní a námořní dopravy
class TransportFactory(ABC):
    @abstractmethod
    def create_land_transport(self) -> LandTransport:
        # Abstraktní metoda pro vytváření pozemní dopravy
        pass

    @abstractmethod
    def create_sea_transport(self) -> SeaTransport:
        # Abstraktní metoda pro vytváření námořní dopravy
        pass

# 9. Konkrétní továrna pro pozemní dopravu
class LandTransportFactory(TransportFactory):
    def create_land_transport(self) -> LandTransport:
        # Vytvoříme a vracíme instanci třídy Car (Auto)
        return Car()

    def create_sea_transport(self) -> SeaTransport:
        # Vytvoříme a vracíme instanci třídy Ship (Loď)
        return Ship()

# 10. Konkrétní továrna pro námořní dopravu
class SeaTransportFactory(TransportFactory):
    def create_land_transport(self) -> LandTransport:
        # Vytvoříme a vracíme instanci třídy Bike (Kolo)
        return Bike()

    def create_sea_transport(self) -> SeaTransport:
        # Vytvoříme a vracíme instanci třídy Submarine (Ponorka)
        return Submarine()

# 11. Hlavní část programu
if __name__ == "__main__":
    # Používáme továrnu pro pozemní dopravu
    land_factory = LandTransportFactory()
    car = land_factory.create_land_transport()  # Vytvoříme auto
    ship = land_factory.create_sea_transport()  # Vytvoříme loď

    print(car.drive())  # Výstup: "Car is driving on the road."
    print(ship.sail())  # Výstup: "Ship is sailing on the sea."

    # Používáme továrnu pro námořní dopravu
    sea_factory = SeaTransportFactory()
    bike = sea_factory.create_land_transport()  # Vytvoříme kolo
    submarine = sea_factory.create_sea_transport()  # Vytvoříme ponorku

    print(bike.drive())  # Výstup: "Bike is pedaling on the road."