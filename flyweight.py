"""
The flyweight pattern: https://refactoring.guru/design-patterns/flyweight
"""

"""
Ship object - info + location
"""
import hashlib
from uuid import uuid4
from typing import Dict


class ShipType:
    def __init__(self, ship_type, capacity) -> None:
        self.ship_type = ship_type
        self.capacity = capacity

    def __str__(self):
        return f"Type: {self.ship_type} with a capacity of {self.capacity}."


class ShipFactory():
    _ship_flyweights: Dict[str, ShipType] = {}

    def get_key(self, state):
        joined_keys = "_".join(sorted(state))
        hashed = hashlib.md5(joined_keys.encode())
        return hashed.hexdigest()

    def get_ship_type(self, shared_state) -> ShipType:
        key = self.get_key(shared_state)

        if not self._ship_flyweights.get(key):
            print("ShipFactory cannot find existing Ship, creating a new one...")
            self._ship_flyweights[key] = ShipType(shared_state[0], shared_state[1])
        else:
            print("ShipFactory: reusing existing Ship...")

        return self._ship_flyweights[key]

class Ship:
    def __init__(self, cargo_weight, ship_type) -> None:
        self.uuid = uuid4()
        self.cargo_weight = cargo_weight
        self.ship_type = ship_type

    def add_cargo(self, weight):
        self.cargo_weight = self.cargo_weight + weight

    def unload_cargo(self):
        self.cargo_weight = 0


class ShipTracker:
    _ships: Dict[str, Ship] = {}

    def add_ship_to_tracker(self, factory: ShipFactory, ship_type, capacity, cargo_weight):
        flyweight = factory.get_ship_type([ship_type, capacity])
        ship = Ship(cargo_weight=cargo_weight, ship_type=flyweight)
        self._ships[ship.uuid] = ship
        print(f"Ship with id: {ship.uuid} was created.")
        return ship
    
    def remove_ship_from_tracker(self, ship_id):
        self._ships.pop(ship_id)

    def list_ships(self):
        for id, ship in self._ships.items():
            print(f"ID: {id}, {ship.ship_type}")


if __name__ == "__main__":
    factory = ShipFactory()
    ships = ShipTracker()

    cruiser = ships.add_ship_to_tracker(factory, "cruiseliner", "1000", 10)
    cargo = ships.add_ship_to_tracker(factory, "cargoship", "5000", 1000)
    yacht1 = ships.add_ship_to_tracker(factory, "yacht", "100", 0)
    yacht2 = ships.add_ship_to_tracker(factory, "yacht", "200", 50)
    yacht3 = ships.add_ship_to_tracker(factory, "yacht", "200", 20)
    print("")
    print(f"Yacht 2's cargo = {yacht2.cargo_weight}")
    print(f"Yacht 3's cargo = {yacht3.cargo_weight}")
    yacht2.add_cargo(50)
    print("Cargo added")
    print(f"Yacht 2's cargo = {yacht2.cargo_weight}")

    print("\nList of available ships:")
    ships.list_ships()
    ships.remove_ship_from_tracker(yacht1.uuid)
    print("\nList of available ships:")
    ships.list_ships()
    yacht1 = ships.add_ship_to_tracker(factory, "yacht", "100", 0)

    print("\nList of available ships:")
    ships.list_ships()

    