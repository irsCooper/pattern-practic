from services import Adaptee, Target
from adapters import CompositionAdapter, InheritanceAdapter


def client(target: Target) -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target: Target = Target()
    client(target)
    print("\n")

    adaptee: Adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. ")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the CompositionAdapter:")
    composition_adapter: CompositionAdapter = CompositionAdapter(adaptee)
    client(composition_adapter)
    
    print("\n")

    print("Client: And I can work with it via the CompositionAdapter:")
    adapter = InheritanceAdapter(adaptee)
    client(adapter)