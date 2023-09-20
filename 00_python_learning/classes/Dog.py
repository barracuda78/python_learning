class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + ": Wof-wof!")


sharik = Dog("Sharik", 2)
sharik.bark()
