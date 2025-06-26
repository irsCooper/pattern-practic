import copy


class Prototype(object):
    """
    Задает виды создаваемых объектов с помощью экземпляра-прототипа
    и создает новые объекты путем копирования этого прототипа.
    """
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def delete(self, name):
        del self._objects[name]

    def clone(self, name, attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj 
    

class Bird(object):
    """Bird"""


if __name__ == "__main__":
    prototype: Prototype = Prototype()
    name_bird: str = "bird"

    prototype.register(name_bird, Bird())

    din = prototype.clone(name_bird, {'name': "Din"})
    print(type(din), din.name)
    
    sheldon = prototype.clone(name_bird, {'name': "Sheldon"})
    print(type(sheldon), sheldon.name)