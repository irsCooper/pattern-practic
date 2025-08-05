from abstaract_component import Component
from example import Composite, Line

"""
Компоновщик -- структурный паттерн, позволяющий создать деревл объектов и работать с ним так же, как и с единичным объектом.
Все операции основаны на рекурсии и "суммировании" результатов на ветвях дерева

Когда стоит использовать:
- объект может быть структурировать в виде дерева (часть -> целое)
- на клиенте нужно одинаково трактовать составние и индивидуальные объекты
"""


def client(component: Component) -> None:
    print(f"Result: {component.operation()}", end="")


def client_2(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)

    print(f"Result: {component1.operation()}", end="")

if __name__ == "__main__":
    simple_example: Line = Line()
    client(simple_example)
    print("\n")

    tree_example: Composite = Composite()

    branch1: Composite = Composite()
    branch1.add(Line())
    branch1.add(Line())
    
    branch2: Composite = Composite()
    branch2.add(Line())
    
    tree_example.add(branch1)
    tree_example.add(branch2)
    
    client(tree_example)
    print("\n")
    client_2(tree_example, simple_example)