from __future__ import annotations
from abc import ABC, abstractmethod

class Car:
    def __init__(self) -> None:
        self.transition_state(CarStoppedState())

    def transition_state(self, state: CarState):
        self._state = state
        self._state.context = self

    def accelerate(self):
        self._state.press_accelerator()

    def honk_horn(self):
        self._state.honk_horn()

    def start_car(self):
        self._state.start_car()

    def stop_car(self):
        self._state.stop_car()


class CarState(ABC):
    @property
    def context(self) -> Car:
        return self._context

    @context.setter
    def context(self, context: Car) -> None:
        self._context = context

    @abstractmethod
    def press_accelerator(self) -> None:
        pass

    @abstractmethod
    def honk_horn(self) -> None:
        pass

    @abstractmethod
    def start_car(self) -> None:
        pass
    
    @abstractmethod
    def stop_car(self) -> None:
        pass


class CarStartedState(CarState):
    def press_accelerator(self) -> None:
        print("THE CAR ACCELERATES!")

    def honk_horn(self) -> None:
        print("The horn beeps loudly!")

    def start_car(self) -> None:
        print("The car is already started, nothing happens.")

    def stop_car(self) -> None:
        self.context.transition_state(CarStoppedState())


class CarStoppedState(CarState):
    def press_accelerator(self) -> None:
        print("The car doesn't move...it's stopped...")

    def honk_horn(self) -> None:
        print("The horn beeps loudly...while stationary!")

    def start_car(self) -> None:
        self.context.transition_state(CarStartedState())

    def stop_car(self) -> None:
        print("The car is already stopped, nothing happens.")


if __name__ == "__main__":
    car = Car()
    car.honk_horn()
    car.accelerate()

    car.stop_car()
    car.start_car()

    car.honk_horn()
    car.accelerate()
