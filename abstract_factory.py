from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


"""
Types of car: Sports, Compact, 4x4
Brands: AUDI, BMW, VW
"""

class AbstractCarFactory(ABC):

    @abstractmethod
    def create_sports_car(self) -> Vehicle:
        pass

    @abstractmethod
    def create_compact_car(self) -> Vehicle:
        pass


class BMWFactory(AbstractCarFactory):
    """
    Creates the BMW family of vehicles.
    """

    def create_sports_car(self) -> Vehicle:
        return SportsCar(no_of_doors=3)
    
    def create_compact_car(self) -> Vehicle:
        return CompactCar(no_of_doors=3)
    

class Vehicle(ABC):
    """
    ABC Vehicle interface.
    """
    def __init__(self, no_of_doors) -> None:
        self.no_of_doors = no_of_doors
    
    @property
    def no_of_doors(self):
        return self._no_of_doors
    
    @no_of_doors.setter
    def no_of_doors(self, no_of_doors):
        self._no_of_doors = no_of_doors

    @abstractmethod
    def drive(self) -> str:
        pass


class SportsCar(Vehicle):
    """
    Sports Car Class
    """
    def drive(self):
        return "The sports car was driven..."


class CompactCar(Vehicle):
    """
    Sports Car Class
    """
    def drive(self):
        return "The compact car was driven..."


def car_creator(factory: AbstractCarFactory):
    sport = factory.create_sports_car()    
    compact = factory.create_compact_car()

    return (sport, compact)


if __name__ == "__main__":
    factory = BMWFactory()
    cars = car_creator(factory)
    for car in cars:
        print(f"Type of BMW: {type(car)}, has {car.no_of_doors} doors.")
