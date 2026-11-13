from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "13.99 pH (Basic/Alkaline)"

class TempSensor(Sensor):
     def get_reading(self):
        return "25.2 deg C"

    

sensor = PHSensor()
sensor1 = TempSensor()

print("--- Lab Inventory System ---")
print("[pH Sensor] Reading: ", (sensor.get_reading()))
print("[Temperature Sensor] Reading: ", (sensor1.get_reading()))
print("----------------------------")
