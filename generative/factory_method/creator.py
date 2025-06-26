from abc import ABC, abstractmethod

from product import Car, Boat, Product

class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        raise NotImplementedError

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"


class CarCreator(Creator):
    def factory_method(self) -> Product:
        return Car()
    
class BoatCreator(Creator):
    def factory_method(self) -> Product:
        return Boat()
    
    