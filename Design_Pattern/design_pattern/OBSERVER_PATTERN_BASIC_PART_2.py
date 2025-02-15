from abc import ABC, abstractmethod
import weakref  # weakref can be used to prevent strong reference cycles in observer patterns
from typing import Set

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, weather_data: "WeatherData"):
        pass

# Data class to hold weather information
class WeatherData:
    def __init__(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def __str__(self):
        return f"Temperature: {self.temperature}°C, Humidity: {self.humidity}%, Pressure: {self.pressure} hPa"

# Subject class (WeatherStation)
class WeatherStation:
    def __init__(self):
        self._observers: Set[Observer] = set()  # Using a set to store unique observers
        self._weather_data: WeatherData = WeatherData(0.0, 0.0, 0.0)

    def add_observer(self, observer: Observer):
        self._observers.add(observer)

    def remove_observer(self, observer: Observer):
        self._observers.discard(observer)

    @property
    def weather_data(self) -> WeatherData:
        return self._weather_data

    @weather_data.setter
    def weather_data(self, data: WeatherData):
        self._weather_data = data
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._weather_data)

# Concrete Observers (Devices)
class MobileDevice(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, weather_data: WeatherData):
        print(f"{self.name} received weather update: {weather_data}")

class DesktopDevice(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, weather_data: WeatherData):
        print(f"{self.name} received weather update: {weather_data}")

class TabletDevice(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, weather_data: WeatherData):
        print(f"{self.name} received weather update: {weather_data}")

# Simulating the scenario
if __name__ == "__main__":
    # Create WeatherStation
    weather_station = WeatherStation()
    
    # Create devices
    mobile = MobileDevice("Mobile")
    desktop = DesktopDevice("Desktop")
    tablet = TabletDevice("Tablet")
    
    # Subscribe devices
    weather_station.add_observer(mobile)
    weather_station.add_observer(desktop)
    weather_station.add_observer(tablet)
    
    # Change weather data
    print("Setting weather data to Temperature: 25°C, Humidity: 60%, Pressure: 1015 hPa...")
    weather_station.weather_data = WeatherData(25, 60, 1015)
    
    print("\nSetting weather data to Temperature: 30°C, Humidity: 55%, Pressure: 1012 hPa...")
    weather_station.weather_data = WeatherData(30, 55, 1012)
    
    # Unsubscribe one device
    print("\nTablet is unsubscribing...")
    weather_station.remove_observer(tablet)
    
    # Change weather data again
    print("\nSetting weather data to Temperature: 28°C, Humidity: 58%, Pressure: 1013 hPa...")
    weather_station.weather_data = WeatherData(28, 58, 1013)
