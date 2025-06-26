import copy


class SomeCommponent:
    def __init__(
            self,
            some_int,
            some_list_of_objects,
            some_circular_ref
        ):
            self.some_int = some_int
            self.some_list_of_objects = some_list_of_objects
            self.some_circular_ref = some_circular_ref

    def __copy__(self):
        some_list_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(
            self.some_int, some_list_objects, some_circular_ref
        )

        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
                memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(
              self.some_int, some_list_of_objects, some_circular_ref
        )

        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new