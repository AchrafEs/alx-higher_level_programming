`0x0A-python-inheritance`

Inheritance is an important concept in object-oriented programming (OOP) that allows classes to inherit attributes
and methods from other classes. In Python, a class can inherit from another class, which is known as the superclass
or parent class, to create a new class called the subclass or child class.

The child class inherits all the attributes and methods of the parent class, and it can also add its own unique
attributes and methods or override the ones inherited from the parent class.

an example to illustrate inheritance in Python:
```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is making a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} is barking.")


# Creating an instance of the Animal class
animal = Animal("Generic Animal")
animal.speak()  # Output: "Generic Animal is making a sound."

# Creating an instance of the Dog class
dog = Dog("Buddy", "Golden Retriever")
dog.speak()  # Output: "Buddy is barking."
```

In the above example, the Animal class is the parent class, and it has an __init__ method and a speak method.
The Dog class is the child class, which inherits from the Animal class using the parentheses after the class
name (class Dog(Animal)). The Dog class also has its own __init__ method and a speak method, which overrides
the speak method inherited from the Animal class.

By using the super() function in the Dog class's __init__ method, we can call the __init__ method of the parent
class and pass the necessary arguments (name in this case) to initialize the inherited attribute.

Inheritance helps in code reusability and promotes a hierarchical organization of classes. It allows us to define
common behaviors in a parent class and extend or modify them in the child classes, promoting code organization
and maintenance.
