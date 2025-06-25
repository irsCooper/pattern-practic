from creator import BoatCreator, CarCreator, Creator


def example(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")
    

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    example(CarCreator())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    example(BoatCreator())