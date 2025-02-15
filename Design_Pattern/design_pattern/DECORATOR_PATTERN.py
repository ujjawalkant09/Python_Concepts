"""
Decorator pattern :


"""

from abc import ABC, abstractmethod

class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass

class MargheritaPizza(BasePizza):
    def cost(self):
        return 100

class Farmhouse(BasePizza):
    def cost(self):
        return 200
    
class BigPizza(BasePizza):
    def cost(self):
        return 300
    

class ToppingDecorator(BasePizza):
    def __init__(self, basepizza):
        self.basepizza = basepizza
        
    @abstractmethod
    def cost(self):
        pass

class ExtraCheese(ToppingDecorator):
    def cost(self):
        return self.basepizza.cost() + 10

class ExtraVeggies(ToppingDecorator):
    def cost(self):
        return self.basepizza.cost() + 20

class ChickenCorn(ToppingDecorator):
    def cost(self):
        return self.basepizza.cost() + 30
    

# Creating a pizza with multiple toppings
pizza = ExtraVeggies(ChickenCorn(BigPizza()))
print(pizza.cost())  # Output: 350
