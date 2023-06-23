from __future__ import annotations
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    ABC Vehicle interface.
    """

    @abstractmethod
    def drive(self) -> str:
        pass

    @abstractmethod
    def refuel(self) -> str:
        pass


class Car(Vehicle):
    def drive(self) -> str:
        return "The car drove..."

    def refuel(self) -> str:
        return "The car refuelled..."


class EBike(Vehicle):
    def drive(self) -> str:
        return "The EBike was ridden..."

    def refuel(self) -> str:
        return "The EBike was charged..."


class VehicleFactory(ABC):
    """
    Factory class declares the factory method that is supposed
    to return an object of a Vehicle class.
    """

    @abstractmethod
    def factory_method(self) -> Vehicle:
        pass

    def drive(self) -> str:
        """ """

        vehicle = self.factory_method()

        result = vehicle.drive()
        return result

    def refuel(self) -> str:
        vehicle = self.factory_method()
        result = vehicle.refuel()
        return result


class CarCreator(VehicleFactory):
    def factory_method(self):
        return Car()


class EBikeCreator(VehicleFactory):
    def factory_method(self):
        return EBike()


def client_code(creator: VehicleFactory):
    print(f"{creator.drive()}")
    print(f"{creator.refuel()}")


if __name__ == "__main__":
    client_code(EBikeCreator())
    client_code(CarCreator())
