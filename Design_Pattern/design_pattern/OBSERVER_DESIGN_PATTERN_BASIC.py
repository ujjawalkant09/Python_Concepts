"""
Okay So I am implementing Weather Station Notification System to understand Observer_Design_Pattern

Requirements:

The WeatherStation (subject) maintains a temperature value.

Multiple devices (observers), such as Mobile, Desktop, and Tablet, are subscribed to
         the WeatherStation.

Whenever the temperature changes, all subscribed devices should be automatically notified 
         with the updated temperature.

Devices should have the ability to unsubscribe from receiving updates at any time.


Tasks:

Ensure that adding or removing observers does not affect other parts of the system.
Simulate a scenario where:

Three devices subscribe to the WeatherStation.

The temperature changes, all devices should receive updates.

One device unsubscribes, and another temperature change occurs.

Only the remaining devices receive the update.

"""

from abc import ABC,abstractmethod
import pdb 


# class generic_observer(ABC):
#     @abstractmethod
#     def update_info(self,list_of_observer):
#         pass

# class observer_1(generic_observer):
#     def update_info(self, list_of_observer):
#          for value in list_of_observer:
#              print("I am being updated")

class Devices(ABC):
    @abstractmethod
    def update_temperature(self,new_temp):
        pass


class Macbook(Devices):
    def update_temperature(self, new_temp):
        print("new temp noted Macbook")

class Window(Devices):
    def update_temperature(self, new_temp):
        print("new temp noted Window")

class Iphone(Devices):
    def update_temperature(self, new_temp):
        print("new temp noted Iphone")

class Android(Devices):
    def update_temperature(self, new_temp):
        print("new temp noted Android")



class DeviceHelper:
    def __init__(self):
        self.list_of_devices = []
    
    def add_devices(self,device:Devices):
         self.list_of_devices.append(device)
    
    def remove_devices(self,device:Devices):
        if device in self.list_of_devices:
            self.list_of_devices.remove(device)
        else:
            print(f"{device} this device is not in the list")
    
    def update_devices(self,new_temp):
        for device in self.list_of_devices:
            device.update_temperature(new_temp)





# WeatherStation
class WeatherStation:
    def __init__(self,temp,device_helper):
        self.temperature = temp
        self.device_helper = device_helper
    
    def update_temperature(self,new_val):
        if new_val != self.temperature:
            # Notify ALl the devices 
            self.device_helper.update_devices(new_val)
            self.temperature = new_val
        else:
            print("Don't notify the devices ")




dev_help = DeviceHelper()
dev_help.add_devices(Iphone())
dev_help.add_devices(Macbook())

weastartion = WeatherStation(10,dev_help)
weastartion.update_temperature(20)

pdb.set_trace()
