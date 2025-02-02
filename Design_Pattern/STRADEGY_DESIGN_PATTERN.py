"""
Strategy Design Pattern

is a relationship (learn how uml works )
has a relationship 


"""

from abc import abstractmethod,ABC
from dataclasses import dataclass

@dataclass
class Item:
      Name:str
      Description: str
      price : int 


class ResturentsItems(ABC):
    @abstractmethod
    def calculate_tax(self,items:list[Item]):
        pass 


class GST18PERCENT(ResturentsItems):
     def calculate_tax(self,items:list[Item]):
          total_price = 0
          for item in items:
               total_price += item.price
          return 0.18*total_price
     

class GST12PERCENT(ResturentsItems):
     def calculate_tax(self,items:list[Item]):
          total_price = 0
          for item in items:
               total_price += item.price
          return 0.12*total_price
     
class GST10PERCENT(ResturentsItems):
     def calculate_tax(self,items:list[Item]):
          total_price = 0
          for item in items:
               total_price += item.price
          return 0.10*total_price
     
class ResturentHelper:
    def __init__(self):
          self.items : list[Item] = []
    
    def add_items(self,itm:Item):
         self.items.append(itm)
         print(self.items)
    
    def calculate_tax(self,obj:ResturentsItems):
         price = obj.calculate_tax(self.items)
         print(price)


if __name__ == "__main__":
     res_help = ResturentHelper()
     res_help.add_items(Item(Name="Red Bulls",Description="Gives You Wings",price=123))
     res_help.calculate_tax(GST10PERCENT())



    
             
     

