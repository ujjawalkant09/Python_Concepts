"""
roughf works --

Design a parking lot

Parking spot should be nearest 

Parking Spot
Different type of spot :
   -> Two wheeler 
   -> Three wheeler
   -> Four wheeler

Exit Gate
On exit gate we will calculate the fair
Payments stradegy
- Hourly based charge 
- Min based charge 
- Mix


identify the object 
- Vechile -> (Vechine Number , Vechile Type (enum -> {Two_wheeler and Four_wheeler}))
- Ticket -> Entrytime , ParkingSpot
- Entrance Gate -> Find parking space , update parking space , Generate Ticket
- Parking Spot -> {id, is_empty, vehicle_info , price, Type}  (as of now there will be two type of parking spot Two_wheeler and Four_wheeler)
- Exit Gate -> {cost calculation , payment , update parking spot}

There are 2 approch 
1. Top to bottom 
2. Bottom to up 

"""

from abc import ABC

class ParkingSpot:
    def __init__(self,id,is_empty,vehicle_info,price,type):
        self.id : int = id
        self.is_empty : bool = is_empty
        self.vehicle_info = vehicle_info
        self.price = price
        self.type = type
    
    def parkvechile(self,vechile):
        self.is_empty = False
        self.vehicle_info = vechile
    
    def removevechile(self,vechile):
        self.is_empty = True
        self.vehicle_info = None

class ParkingSpotManager:
    #   List of Parking Spot 
    def __init__(self):
        ""
    def find_parking_space(self):
        ""
    def add_parking_space(self):
        ""
    def remove_parking_space(self):
        ""
    def park_vechile(self):
        ""
    def remove_vechile(self):
        ""

class ParkingStradegy:
    ""


class TwoWheelerManager:
    ""

class FourWheelerManager:
    ""


class wheelerspot(ABC):
    @staticmethod
    def price(self):
        pass

class TwoWheelerSpot(wheelerspot):
    def price(self):
        price = 10
        return price

class FourWheelerSpot(wheelerspot):
    def price(self):
        price = 20
        return price

class SixWheelerSpot(wheelerspot):
    def price(self):
        price = 30
        return price


class Vechile:
    "" 


class ExitGate:
    ""


class EntranceGate:
    ""



class Ticket:
    ""
