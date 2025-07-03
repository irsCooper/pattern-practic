from typing import List
from abstaract_component import Component


class Line(Component):
    def operation(self):
        return "Line"
    
    
class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None 

    def is_composite(self):
        return True 
    
    def operation(self) -> str:
        results: List = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"
    