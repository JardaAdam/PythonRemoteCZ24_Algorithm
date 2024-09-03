from abc import ABC, abstractmethod

class LandTransport(ABC):
    @abstractmethod
    def drive(self):
        pass

class SeaTransport(ABC):
    @abstractmethod
    def sail(self):
        pass

class Car(LandTransport):
    def drive(self):
        return "Car is driving on the road."

class Bike(LandTransport):
    def drive(self):
        return "Bike is pedaling on the road."

class Ship(SeaTransport):
    def sail(self):
        return "Ship is sailing on the sea."

class Submarine(SeaTransport):
    def sail(self):
        return "Submarine is navigating underwater."

class TransportFactory(ABC):
    @abstractmethod
    def create_land_transport(self) -> LandTransport:
        pass

    @abstractmethod
    def create_sea_transport(self) -> SeaTransport:
        pass


class LandTransportFactory(TransportFactory):
    def create_land_transport(self) -> LandTransport:
        return Car()  # Můžeme také vrátit Bike() dle potřeby.

    def create_sea_transport(self) -> SeaTransport:
        return Ship()  # Výchozí produkt pro pozemní továrnu, ale vytvoří také námořní dopravu.


class SeaTransportFactory(TransportFactory):
    def create_land_transport(self) -> LandTransport:
        return Bike()  # Výchozí produkt pro námořní továrnu, ale vytvoří také pozemní dopravu.

    def create_sea_transport(self) -> SeaTransport:
        return Submarine()  # Můžeme také vrátit Ship() dle potřeby.

if __name__ == "__main__":
    # Použijeme továrnu pro pozemní dopravu
    land_factory = LandTransportFactory()
    car = land_factory.create_land_transport()
    ship = land_factory.create_sea_transport()

    print(car.drive())  # Výstup: "Car is driving on the road."
    print(ship.sail())  # Výstup: "Ship is sailing on the sea."

    # Použijeme továrnu pro námořní dopravu
    sea_factory = SeaTransportFactory()
    bike = sea_factory.create_land_transport()
    submarine = sea_factory.create_sea_transport()

    print(bike.drive())  # Výstup: "Bike is pedaling on the road."
    print(submarine.sail())  # Výstup: "Submarine is navigating underwater."