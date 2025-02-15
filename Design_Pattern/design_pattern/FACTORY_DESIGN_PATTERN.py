"""
FACTORY DESIGN PATTERN

What is the Factory Design Pattern?
The Factory Pattern is a creational design pattern that provides an interface for creating objects in a superclass, 
but allows subclasses to alter the type of objects that will be created.

Instead of calling a constructor directly, you use a special method (factory method) to create instances.


When to Use?
When the client code should not need to know the class of the object it needs.
When creating objects is complex or requires logic not appropriate in the constructor.
When you want to provide loose coupling between the client code and the classes used to instantiate objects.



Basic Structure

Creator (Abstract Class)
│
├─ ConcreteCreatorA (Implements factory method to create ProductA)
│
└─ ConcreteCreatorB (Implements factory method to create ProductB)

Product (Abstract Class)
│
├─ ConcreteProductA
└─ ConcreteProductB



"""

from abc import ABC,abstractmethod

# Abstract Product
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Products
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    def get_shape(self,shape_type):
        if shape_type=="circle":
            return Circle()
        elif shape_type=="square":
            return Square()
        else:
            return "shape_type not define"
        
# Client Code
factory = ShapeFactory()
shape_1 = factory.get_shape("circle")
print(shape_1.draw())

shape_2 = factory.get_shape("square")
print(shape_2.draw())


