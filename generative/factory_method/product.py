# from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass 


class Car(Product):
    def operation(self) -> str:
        return "{Result of the Car}"
    
class Boat(Product):
    def operation(self) -> str:
        return "{Result of the Boat}"
    
