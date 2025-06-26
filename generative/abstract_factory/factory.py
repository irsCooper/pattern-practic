from abc import ABC, abstractmethod

from chair import AbstractChair, ChairPlastic, ChairWooden
from wardrobe import AbstractWardrobe, WardrobePlastic, WardrobeWooden

class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        raise NotImplementedError

    @abstractmethod
    def create_wardrobe(self) -> AbstractWardrobe:
        raise NotImplementedError


class WoodenFactory(AbstractFactory):
    def create_chair(self) -> ChairWooden:
        return ChairWooden()
    
    def create_wardrobe(self) -> WardrobeWooden:
        return WardrobeWooden()
    

class PlasticFactory(AbstractFactory):
    def create_chair(self) -> ChairPlastic:
        return ChairPlastic()
    
    def create_wardrobe(self) -> WardrobePlastic:
        return WardrobePlastic()