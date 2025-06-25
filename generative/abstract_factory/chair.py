from abc import ABC, abstractmethod

from wardrobe import AbstractWardrobe

class AbstractChair(ABC):
    @abstractmethod
    def useful_function(self) -> str:
        pass 

    @abstractmethod
    def another_useful_function(self, collaborator: AbstractWardrobe) -> str:
        pass


class ChairWooden(AbstractChair):
    def useful_function(self) -> str:
        return "The result of Chair Wooden"
    
    def another_useful_function(self, collaborator: AbstractWardrobe) -> str:
        res = collaborator.useful_function()
        return f"The result of the Wardrobe collaborating with the ({res})"
    
    
class ChairPlastic(AbstractChair):
    def useful_function(self) -> str:
        return "The result of Chair Plastic"
    
    def another_useful_function(self, collaborator: AbstractWardrobe) -> str:
        res = collaborator.useful_function()
        return f"The result of the Wardrobe collaborating with the ({res})"