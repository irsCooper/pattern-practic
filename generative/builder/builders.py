from abc import ABC, abstractmethod

from products import House, Igloo


class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass 

    @abstractmethod
    def set_window_type(self):
        pass 

    @abstractmethod
    def set_door_type(self):
        pass 

    @abstractmethod
    def set_num_floor(self):
        pass 

    
class HouseBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = House()

    @property
    def product(self) -> House:
        product = self._product
        self.reset()
        return product
    
    def set_window_type(self):
        self._product.windows_type = "Wooden"

    def set_door_type(self):
        self._product.door_type = "Wooden"

    def set_num_floor(self):
        self._product.floor = 2


class IglooBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = Igloo()

    @property
    def product(self) -> Igloo:
        product = self._product
        self.reset()
        return product
    
    def set_window_type(self):
        self._product.windows_type = "Snow"

    def set_door_type(self):
        self._product.door_type = "Snow"

    def set_num_floor(self):
        self._product.floor = 1