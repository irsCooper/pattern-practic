import copy
from some_component import SomeCommponent
from self_referencing_entity import SelfReferencingEntity


if __name__ == "__main__":
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeCommponent(40, list_of_objects, circular_ref)

    shallow_copied_component = copy.copy(component)

    new_object_str = "new object"
    shallow_copied_component.some_list_of_objects.append(new_object_str)
    if component.some_list_of_objects[-1] == new_object_str:
        print("some_list_of_objects adds it to `component`'s")
    else:
        print("some_list_of_objects doesn't add it to `component`'s")