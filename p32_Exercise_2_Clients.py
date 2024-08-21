"""Exercise 2.1: Clients

Imagine we have a store.
Implement the store's customer abstract class and 3 classes inheriting from it.
There are three groups of customers:
- Women
- Men
- Children

Each of these groups should be addressed in a different way:
women as Madam, men as Mr, and no prefixes for children.

Each inherited class should have its own string representation.
"""


import abc


class Client(abc.ABC):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class Woman(Client):
    def __str__(self) -> str:
        return f"Madam {self.first_name} {self.last_name}"


class Man(Client):
    def __str__(self) -> str:
        return f"Mr {self.first_name} {self.last_name}"


class Child(Client):
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


"""Exercise 2.2: FIFO queue
This exercise creates a queue class using a list. 
In this case, adding an element should consist of using the append method 
(adding an object to the Horsesc queue). 
The removal of an element should be accomplished by removing the first element 
from the list by using pop (the object leaves the queue at the beginning).
"""


class FifoList:
    def __init__(self):
        self.lst = []

    def append(self, data):
        self.lst.append(data)

    def pop(self):
        if len(self.lst):
            return self.lst.pop(0)
        return None


"""Exercise 2.3: Cash register
Implement an instance of a class that simulates store operations. 
The cash register should have a queue and be able to join and service new customers. 
Use the implemented FIFO queue class.
"""


class CashRegister:
    def __init__(self):
        self.queue = FifoList()

    def add_client(self, client: Client):
        self.queue.append(client)

    def process(self) -> Client:
        client = self.queue.pop()
        print(f"Process client: {client}")
        return client


if __name__ == '__main__':
    client1 = Woman("Anna", "Johnson")
    client2 = Man("John", "Smith")
    client3 = Child("Chris", "Novak")

    print(client1)
    print(client2)
    print(client3)

    cr = CashRegister()
    cr.add_client(client1)
    cr.add_client(client2)
    cr.add_client(client3)

    cr.process()
    cr.process()
    cr.process()

