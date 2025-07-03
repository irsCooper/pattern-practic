from abc import ABC, abstractmethod


class Component(ABC):
    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @abstractmethod
    def operation(self):
        raise NotImplementedError
    
    def add(self, obj): 
        raise NotImplementedError
    
    def remove(self, obj):
        raise NotImplementedError
    
    def get_children(self, index: int):
        raise NotImplementedError

    def is_composite(self) -> bool:
        return False