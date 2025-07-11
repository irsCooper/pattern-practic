class SingletonMeta(type):
    _instances = {}

    def __init__(cls, *args, **kwargs):
        super(SingletonMeta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Singleton(metaclass=SingletonMeta):
    def some_buisiness_logic(self):
        return "Some logic"
    

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance")
    else:
        print("Singleton faied")