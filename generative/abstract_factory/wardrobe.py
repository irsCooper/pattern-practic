from abc import ABC, abstractmethod

class AbstractWardrobe(ABC):
    @abstractmethod
    def useful_function(self) -> str:
        raise NotImplementedError


class WardrobeWooden(AbstractWardrobe):
    def useful_function(self) -> str:
        return "The result of Wardrobe Wooden"
    
class WardrobePlastic(AbstractWardrobe):
    def useful_function(self) -> str:
        return "The result of Wardrobe Plastic"