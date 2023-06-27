`0x06-python-classes`

In Python, a class is a blueprint for creating objects (instances) that have their own set of attributes
(variables) and behaviors (methods). It serves as a template or a structure for creating objects with
similar properties and functionalities.

To define a `class` in Python, you use the class keyword followed by the class name. Here's a basic example
of a class definition:

```
class MyClass:
pass
```
In this example, `MyClass` is the name of the class. The pass statement is a placeholder, indicating that
the class doesn't have any attributes or methods defined yet.

To create an object (instance) of a class, you use the class name followed by parentheses, like calling a function.
This process is called instantiation. Here's an example:

```
obj = MyClass()
```
Now, let's explore how to define attributes and methods within a class.

`Attributes:`

Attributes represent the data (variables) associated with a class. These variables can hold values that are specific
to each instance of the class. You define attributes within a class by assigning values to them using the `self` keyword.
The `self` keyword represents the instance of the class and allows you to access its attributes and methods.
Here's an example of defining attributes:

```
class MyClass:
    def __init__(self):
        self.name = "John"
        self.age = 25
```
In this example, `name` and `age` are attributes of the `MyClass` class. They are assigned initial values within the
special method `__init__`, which is called a constructor. The `self` parameter refers to the instance being created,
allowing you to set specific attribute values for each instance.

`Methods:`

Methods are functions defined within a class. They define the behaviors or actions that objects of the class
can perform. You can define methods by creating functions within the class, and they have access to the instance
attributes using the `self` parameter. Here's an example of defining methods:

```
class MyClass:
    def __init__(self):
        self.name = "John"
        self.age = 25

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```
In this example, `greet()` is a method defined within the MyClass class. It uses the `self.name` and `self.age`
attributes to display a greeting message specific to each instance.

To use the class and its methods or attributes, you can create objects and call their methods or access their
attributes. Here's an example:

```
obj = MyClass()
obj.greet()  # Output: Hello, my name is John and I am 25 years old.
```
This creates an instance of `MyClass` called `obj` and calls its `greet()` method, resulting in the greeting message
being printed.

Classes provide a way to organize and structure your code, allowing you to create reusable and modular components.
They are a fundamental part of object-oriented programming and enable you to model real-world entities and their
interactions in your programs.
