from director import HouseDirector
from builders import HouseBuilder


if __name__ == "__main__":
    houseDirector: HouseDirector = HouseDirector()
    builder: HouseBuilder = HouseBuilder()

    houseDirector.builder = builder

    print("Standart basic house: ")
    houseDirector.build_minimal_viable_house()
    print(builder.product.__dict__)

    print("\n")

    print("Standart full feature house: ")
    houseDirector.build_full_featured_house()
    print(builder.product.__dict__)

    print("\n")

    print("Custom product: ")
    builder.set_window_type()
    print(builder.product.__dict__)