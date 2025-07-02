class Singleton:
    __instance = None 

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance
    

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print(s1, s2, "\n")
        print("Singleton works, both variables contain the same instance")
    else:
        print("Singleton faied")