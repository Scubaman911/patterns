from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class ABCSubscriptionManager(ABC):
    """
    Subscription interface declares a set of methods
    for managing subscribers.
    """

    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class SubscriptionManager(ABCSubscriptionManager):
    _important_value: int = None
    _observers: List[Observers] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def change_important_value(self, value):
        self._important_value = value
        print(f"Important value is now {value}")
        self.notify()

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, publisher: SubscriptionManager) -> None:
        """
        Receive update from subject.
        """
        pass


class ConcreteObserverA(Observer):
    def update(self, publisher: SubscriptionManager) -> None:
        if publisher._important_value < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, publisher: SubscriptionManager) -> None:
        if publisher._important_value == 0:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    sub_mngr = SubscriptionManager()

    subscriber1 = ConcreteObserverA()
    subscriber2 = ConcreteObserverB()
    sub_mngr.subscribe(subscriber1)
    sub_mngr.subscribe(subscriber2)

    sub_mngr.change_important_value(2)
    sub_mngr.change_important_value(1)
    sub_mngr.change_important_value(0)