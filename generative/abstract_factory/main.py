from factory import AbstractFactory, PlasticFactory, WoodenFactory


def client(factory: AbstractFactory, name_factory_type: str) -> None:
    print(f'Client: Testing client code with the {name_factory_type} factory type')

    chair = factory.create_chair()
    wardrobe = factory.create_wardrobe()

    print(f"{wardrobe.useful_function()}")
    print(f"{chair.another_useful_function(wardrobe)}", end="\n\n")


if __name__ == "__main__":
    client(WoodenFactory(), "Wooden")
    client(PlasticFactory(), "Plastic")
    