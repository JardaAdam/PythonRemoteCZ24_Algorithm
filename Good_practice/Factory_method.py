# v zakladni tride nic nedela jenom specifikuje co musi ta class umet.

# Dobra varianta pro data Archytecty

#

class Transport:
    def start_transport(self):
        raise NotImplementedError


class Car(Transport):
    def start_transport(self):
        return "Starting the car. Driving on the road!"


class Ship(Transport):
    def start_transport(self):
        return "Starting the ship. Sailing on the water!"


def create_transport(transport_type):
    if transport_type == "car":
        return Car()
    elif transport_type == "ship":
        return Ship()
    else:
        raise ValueError(f"Unknown transport type: {transport_type}")


class TransportFactory:
    pass


if __name__ == "__main__":
    factory = TransportFactory()

    car = create_transport("car")
    ship = create_transport("ship")

    print(car.start_transport())  # Starting the car. Driving on the road!
    print(ship.start_transport())  # Starting the ship. Sailing on the water!


class Transport:
    def move(self):
        raise NotImplementedError


class Car(Transport):
    def move(self):
        return "I'm driving"


class Bike(Transport):
    def move(self):
        return "I'm cycling"


cervene_kolo = Bike()
cervene_kolo.move()
print(cervene_kolo.move())
