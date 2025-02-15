"""

what is abstarct class and there decorator 
@abstractmethod
@abstractclassmethod
@abstractproperty
@abstractstaticmethod

Abstract Class -> This class can't be directly instantiated. We use this as templete or interface for subclasses.
                  To force your subclasses to implement certain methods.

Abstract Method/Property :-> A placeholder for a method/property. If a class has any abstarct method, it is considered an abstract class. 
                            subclass must provide concrete implementations to become instantialbe.


To create an abstract class, you typically inherit from ABC (or set metaclass=ABCMeta) and use abstract decorators on the 
methods/properties that you want to be mandatory in subclasses.


Overview of Each Decorator


----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

1. @abstractmethod

Used to mark instance methods as abstract.
Subclasses must implement this method.

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

2. @abstractclassmethod
Same as @abstractmethod but for class methods (@classmethod).
Subclasses must implement a class method with the same signature.
hint - diff between @classmethod and @staticmethod

Class Method (@classmethod): {in simpler word we can initialize it like static_methods but it can access class vlaues }
Receives the class itself (cls) as the first argument.
Can access or modify class-level attributes.
Signature looks like def some_method(cls, ...).

Static Method (@staticmethod):
Receives no automatic first argument (no self, no cls).
Cannot directly access instance or class state—unless it’s passed in explicitly as a parameter.
Essentially a regular function that just lives inside a class’s namespace for organizational purposes.

class Example:
    class_level_count = 0

    def __init__(self):
        # Increment the class-level counter each time an instance is created
        Example.class_level_count += 1

    @classmethod
    def get_class_count(cls):
        
        'A class method that uses 'cls' to access class attributes or methods.'

        return cls.class_level_count

    @staticmethod
    def greet(name):
        '
        A static method that doesn't receive 'self' or 'cls'. 
        It's just a utility function placed under the class's namespace.
        '
        return f"Hello, {name}!"

# ------------------------ Usage -------------------------
# You can call both class and static methods on the class directly:
print(Example.get_class_count())  # 0 initially

obj1 = Example()
obj2 = Example()
print(Example.get_class_count())  # 2, after creating two instances

# Static method is just like a normal function in this context
print(Example.greet("Alice"))     # "Hello, Alice!"



----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

3. @abstractstaticmethod
Same as @abstractmethod but for static methods (no self or cls argument).


----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
4. @abstractproperty
Marks a property as abstract.
Subclasses must implement this property (often via @property).

What Is an Abstract Property?

it is @abstractmethod + @property -> @abstractproperty

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
what is @property
In Python, @property is a built-in decorator that lets you turn a method into a read-only attribute, making your code look more elegant and pythonic.
Essentially, it allows you to:

Expose methods as attributes (so you call them without parentheses: obj.attribute instead of obj.attribute()).
Provide getter, setter, and deleter functionality for a single attribute name, but in a controlled and encapsulated way.
Below is a simple breakdown, followed by an illustrative example.



Reasoned for a second
In Python, @property is a built-in decorator that lets you turn a method into a “read-only” attribute, making your code look more elegant and pythonic. Essentially, it allows you to:

Expose methods as attributes (so you call them without parentheses: obj.attribute instead of obj.attribute()).
Provide getter, setter, and deleter functionality for a single attribute name, but in a controlled and encapsulated way.
Below is a simple breakdown, followed by an illustrative example.


A Quick Motivational Example
before @property
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_area(self):
        return 3.14159 * (self._radius ** 2)

circle = Circle(5)
print(circle.get_area())  # 78.53975

To get the area, you call a method: circle.get_area().
If you wanted a read-only area attribute, you might just define circle.area as a variable. 
But that would only be correct at the time you created it unless you updated it every time radius changed.



With @property, you can turn get_area into a calculated attribute that you access like a normal attribute:
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

circle = Circle(5)
print(circle.area)  # 78.53975, but accessed like an attribute

Now circle.area looks like a read-only attribute, but under the hood, its still a method call that computes the area. 
This is more intuitive for many use cases.




2. How @property Works
when you put @property above a method:

1. That method become the getter for an attribute with the same name.
2. This attribute is read-only unless you add a setter or deleter 

Example with a Setter


But area is derived (width * height), so how can you change the area if its supposed to set something in width/height?

Possible approach: You might decide that if the user sets area, you will change height to keep width the same (for instance).


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @area.setter
    def area(self, new_area):
        # Let's keep the width fixed, and adjust the height
        self._height = new_area / self._width

rect = Rectangle(10, 2)
print(rect.area)  # 20

rect.area = 50    # calls the setter
print(rect.area)  # 50
print(rect._height)  # 5.0

Here, we have a getter (@property) and a setter (@area.setter).
When you do rect.area = 50, it actually calls the setter method, which adjusts the height to 5.0 (since width is 10, 10*5=50).



Accessing Private Attributes
Notice in the code, the actual variables are _width and _height—we often use an underscore prefix to indicate they are internal or private.
@property methods typically serve as a public interface to these private attributes.

4. Why Use @property?

Cleaner, More Pythonic API: Users access attributes like obj.area or obj.species instead of calling obj.get_area() or obj.get_species().

Encapsulation: You can later change how the attribute is computed without breaking existing code. 
Maybe you initially stored an area variable, but then you decide to compute it on the fly. 
As long as the interface remains obj.area, client code doesnt need to change.

Validation: Using a setter (@<name>.setter), you can add validation logic any time someone tries to set that attribute.


Full Example with Getter and Setter

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        ""
        This is a read-write property.
        Reading 'full_name' returns a combination of first and last name.
        ""
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, new_name):
        ""
        Setting 'full_name' splits the input and updates internal first/last name.
        ""
        parts = new_name.split(" ", 1)
        if len(parts) < 2:
            raise ValueError("Please provide both first and last name.")
        self._first_name, self._last_name = parts[0], parts[1]

# Usage
p = Person("John", "Doe")
print(p.full_name)   # "John Doe"

p.full_name = "Jane Smith"  # calls the setter
print(p.full_name)   # "Jane Smith"


Summary ::

@property transforms a class method into a getter that can be accessed like a regular attribute (obj.attribute).

@<property_name>.setter and @<property_name>.deleter allow you to define corresponding setter and deleter behavior 
under the same attribute name, giving you a complete, well-encapsulated interface.

Its a cornerstone of Pythons descriptors feature, enabling you to write code thats both clear 
to read and flexible to change behind the scenes.
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

"""
