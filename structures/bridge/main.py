

"""
Мост -- структурный паттерн, разделяющий логику большого класса на несколько отдельных абстракций, 
которые потом можно развивать (реализовывать) отдельно друг от друга

Абстракция получит ссыылку на объекты другой реализации и будет делегировать им основную работу.
Так как реализации следуют абстракции, их можно взаимозаменять внутри неё

Когда использовать:
- кроссплатформенное приложение с поддержкой разных бд 
- изменения абстракции и реализации не должны сказываться на клиентском коде
- при разделении большого класса с несколькими реализациями некоторой функциональности (кнопка скачать с разным визуалом, например)
- нужно избежать постоянной  привязки абстракции к реализации (реализация может меняться)
"""

from abc import ABC, abstractmethod
import time


class Pizza:
    def __init__(self, name: str, cook_time: int):
        self.name = name
        self.cook_time = cook_time
        self.__isCook = False

    def cook(self) -> None:
        self.__isCook = True

    def isCooked(self) -> bool:
        return self.__isCook 
    


class IOvenImplementor(ABC):
    "Интерфейс для реализации печей разного типа"
    @abstractmethod
    def cook_pizza(self, pizza: Pizza) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_oven_type(self) -> str:
        raise NotImplementedError
    


class ClassicOvenImplementor(IOvenImplementor):
    def __init__(self):
        self.type = "Classic"

    def cook_pizza(self, pizza: Pizza) -> None:
        time.sleep(pizza.cook_time)
        pizza.cook()

    def get_oven_type(self) -> str:
        return self.type



class ElectricalOvenImplementor(IOvenImplementor):
    def __init__(self):
        self.type = "Electrical"

    def cook_pizza(self, pizza: Pizza) -> None:
        time.sleep(pizza.cook_time)
        pizza.cook()

    def get_oven_type(self) -> str:
        return self.type



class Oven: 
    def __init__(self, implementor: IOvenImplementor):
        self.__implementor = implementor

    def cook_pizza(self, pizza: Pizza) -> None:
        print(f"Cooking {pizza.name} pizza for {pizza.cook_time} minutes in {self.__implementor.get_oven_type()} oven type")
        self.__implementor.cook_pizza(pizza)

    def change_implementor(self, implementor: IOvenImplementor) -> None:
        self.__implementor = implementor

    def get_oven_type(self):
        return self.__implementor.get_oven_type()



if __name__ == "__main__":
    first_pizza: Pizza = Pizza("Four cheez", 3)
    second_pizza: Pizza = Pizza("Pepperony", 5)

    implementor: ClassicOvenImplementor = ClassicOvenImplementor()
    oven: Oven = Oven(implementor)

    oven.cook_pizza(first_pizza)
    oven.cook_pizza(second_pizza)

    first_pizza: Pizza = Pizza("Margarita", 4)
    second_pizza: Pizza = Pizza("Salami", 2)

    print("Change implementor")
    new_implementor: ElectricalOvenImplementor = ElectricalOvenImplementor()
    oven.change_implementor(new_implementor)

    oven.cook_pizza(first_pizza)
    oven.cook_pizza(second_pizza)