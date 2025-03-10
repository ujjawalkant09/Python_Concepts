from abc import ABC, abstractmethod
from enum import Enum
import time
from datetime import datetime


# Vehicle Type Enum
class VehicleType(Enum):
    TWO_WHEELER = "Two Wheeler"
    FOUR_WHEELER = "Four Wheeler"
    SIX_WHEELER = "Six Wheeler"


# Vehicle Class
class Vehicle:
    def __init__(self, number: str, vehicle_type: VehicleType):
        self.number = number
        self.vehicle_type = vehicle_type


# Abstract Parking Spot
class ParkingSpot(ABC):
    def __init__(self, spot_id: int, price: float, spot_type: VehicleType):
        self.id = spot_id
        self.is_empty = True
        self.vehicle_info = None
        self.price = price
        self.spot_type = spot_type

    def park_vehicle(self, vehicle: Vehicle):
        if self.is_empty:
            self.is_empty = False
            self.vehicle_info = vehicle
            return True
        return False

    def remove_vehicle(self):
        self.is_empty = True
        self.vehicle_info = None


# Concrete Parking Spots
class TwoWheelerSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, 10, VehicleType.TWO_WHEELER)


class FourWheelerSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, 20, VehicleType.FOUR_WHEELER)


class SixWheelerSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, 30, VehicleType.SIX_WHEELER)


# Ticket Class
class Ticket:
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot):
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.entry_time = datetime.now()


# Parking Spot Manager
class ParkingSpotManager:
    def __init__(self):
        self.spots = {
            VehicleType.TWO_WHEELER: [],
            VehicleType.FOUR_WHEELER: [],
            VehicleType.SIX_WHEELER: [],
        }

    def add_parking_space(self, spot: ParkingSpot):
        self.spots[spot.spot_type].append(spot)

    def find_parking_space(self, vehicle_type: VehicleType):
        for spot in self.spots[vehicle_type]:
            if spot.is_empty:
                return spot
        return None  # No available spot

    def remove_parking_space(self, spot: ParkingSpot):
        self.spots[spot.spot_type].remove(spot)


# Parking Strategy Interface
class ParkingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, entry_time: datetime, exit_time: datetime, price_per_hour: float):
        pass


# Hourly Pricing Strategy
class HourlyStrategy(ParkingStrategy):
    def calculate_fare(self, entry_time, exit_time, price_per_hour):
        duration = (exit_time - entry_time).seconds // 3600
        return max(1, duration) * price_per_hour


# Minute-Based Pricing Strategy
class MinuteStrategy(ParkingStrategy):
    def calculate_fare(self, entry_time, exit_time, price_per_hour):
        duration = (exit_time - entry_time).seconds // 60
        return max(1, duration) * (price_per_hour / 60)


# Mixed Pricing Strategy
class MixedStrategy(ParkingStrategy):
    def calculate_fare(self, entry_time, exit_time, price_per_hour):
        duration = (exit_time - entry_time).seconds
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60

        return (hours * price_per_hour) + (minutes * (price_per_hour / 60)) + (seconds * (price_per_hour / 3600))

# class MixedStrategy(ParkingStrategy):
#     def calculate_fare(self, entry_time, exit_time, price_per_hour):
#         duration = (exit_time - entry_time).seconds
#         hours = duration // 3600
#         minutes = (duration % 3600) // 60
#         return (hours * price_per_hour) + (minutes * (price_per_hour / 60))


# Entrance Gate
class EntranceGate:
    def __init__(self, parking_manager: ParkingSpotManager):
        self.parking_manager = parking_manager

    def generate_ticket(self, vehicle: Vehicle):
        spot = self.parking_manager.find_parking_space(vehicle.vehicle_type)
        if spot:
            spot.park_vehicle(vehicle)
            return Ticket(vehicle, spot)
        else:
            print("No parking space available")
            return None


# Exit Gate
class ExitGate:
    def __init__(self, strategy: ParkingStrategy):
        self.strategy = strategy

    def process_payment(self, ticket: Ticket):
        exit_time = datetime.now()
        total_cost = self.strategy.calculate_fare(ticket.entry_time, exit_time, ticket.parking_spot.price)
        print(f"Vehicle {ticket.vehicle.number} is exiting. Total cost: {total_cost}")
        ticket.parking_spot.remove_vehicle()


# 

# Initialize Parking System
manager = ParkingSpotManager()
manager.add_parking_space(TwoWheelerSpot(1))
manager.add_parking_space(FourWheelerSpot(2))

entrance = EntranceGate(manager)
exit_gate = ExitGate(MixedStrategy())

# Vehicle Enters
vehicle1 = Vehicle("KA-01-1234", VehicleType.TWO_WHEELER)
ticket1 = entrance.generate_ticket(vehicle1)

# Simulate Exit After Some Time
time.sleep(5)  # Simulate some delay
exit_gate.process_payment(ticket1)
