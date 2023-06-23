"""
https://refactoring.guru/design-patterns/bridge
"""
from abc import ABC, abstractmethod

class VehicleController:
    """
    Interface for the control part of two class hierarchies.
    """
    def __init__(self, implementation) -> None:
        self.implementation = implementation

    def drive(self) -> str:
        return f"Base {self.implementation.drive()}"
    
    def refuel(self) -> str:
        return f"Base {self.implementation.refuel()}"
    

class VehicleFlightController(VehicleController):
    def roll(self, degrees):
        return f"Flight {self.implementation.roll(degrees=degrees)}"


class Vehicle(ABC):

    def __init__(self, doors) -> None:
        self.doors = doors

    @property
    def doors(self):
        return self._doors
    
    @doors.setter
    def doors(self, doors):
        self._doors = doors

    def drive(self):
        return f"The {self} drove..."

    def refuel(self):
        return f"The {self} refuelled..."


class BMW(Vehicle):
    def __init__(self, model) -> None:
        super().__init__(doors=5)
        self.model = model

    def __str__(self):
        return "BMW Car"

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model


class Cesna(Vehicle):
    def __init__(self, wings) -> None:
        super().__init__(doors=2)
        self.wings = wings

    def __str__(self):
        return "Cesna Plane"

    @property
    def wings(self):
        return self._wings
    
    @wings.setter
    def wings(self, wings):
        self._wings = wings

    def roll(self, degrees):
        return f"The {self} rolled {degrees} degrees..."


def client_code():
    bmw = BMW(model="420i")
    vehicle_ctrl = VehicleController(bmw)

    print(vehicle_ctrl.drive())
    print(vehicle_ctrl.refuel())

    cesna = Cesna(wings=2)
    flight_ctrl = VehicleFlightController(cesna)

    print(flight_ctrl.drive())
    print(flight_ctrl.refuel())
    print(flight_ctrl.roll(degrees=5))



if __name__ == "__main__":
    client_code()