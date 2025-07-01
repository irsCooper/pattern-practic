from services import Adaptee, Target


class InheritanceAdapter(Target, Adaptee):
    def request(self) -> str:
        return f"InheritanceAdapter: {self.specific_request()[::-1]}"
    
class CompositionAdapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"CompositionAdapter: {self.adaptee.specific_request()[::-1]}"