from builders import Builder


class HouseDirector:
    def __init__(self):
        self._builder = None 

    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_house(self) -> None:
        self.builder.set_door_type()

    def build_full_featured_house(self) -> None:
        self.builder.set_door_type()
        self.builder.set_num_floor()
        self.builder.set_window_type()