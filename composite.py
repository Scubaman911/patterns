"""
https://refactoring.guru/design-patterns/composite/python/example
"""
from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import List


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    @abstractproperty
    def price(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """
        pass


class Product(Component):
    def __init__(self, price) -> None:
        self.price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price


class Phone(Product):
    pass

class Radio(Product):
    pass

class Box(Component):
    def __init__(self) -> None:
        self._children: List[Product] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    @property
    def price(self) -> float:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = 0
        for child in self._children:
            results = results + child.price
        return results


def client_code():
    phone = Phone(10.00)
    radio1 = Radio(20.00)
    radio2 = Radio(20.00)
    radio3 = Radio(20.00)

    big_box = Box()
    small_box = Box()
    small_box.add(phone)
    small_box.add(radio2)

    big_box.add(radio1)
    big_box.add(radio3)
    big_box.add(small_box)

    print(f"The total value of the big box is £{big_box.price:.2f}.")


if __name__ == "__main__":
    client_code()