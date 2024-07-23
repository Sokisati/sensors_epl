from gyro_file import MPUSensor
from barometric_file import BMESensor
from rtc_file import RTCSensor
from gps_file import GPSSensor

    
class SensorDataPack:
    def __init__(self):
        self.lat = 0;
        self.long = 0;
        self.alt = 0;
        self.temperature = 0;
        self.pressure = 0;
        self.altitude = 0;
        self.voltage = 0;
        self.roll = 0;
        self.pitch = 0;
        self.yaw = 0;
        self.dateAndTime = '1/1/2038-00/00/00'
        

class SensorPack:
    
    def __init__(self):
        self.bme = BMESensor();
        self.gyro = MPUSensor();
        self.sensorDataPack = SensorDataPack();
    
    def test(self):
        self.bme.test();
        self.gyro.test();

    def updateSensorDataPack(self):
        self.sensorDataPack.roll = self.gyro.getRoll();
        self.sensorDataPack.pitch = self.gyro.getPitch();
        self.sensorDataPack.yaw = self.gyro.getYaw();
        self.sensorDataPack.temperature = self.bme.getTemp();
        self.sensorDataPack.pressure = self.bme.getPressure();
        self.sensorDataPack.altitude = self.bme.getAlt();
    
    def printDataPack(self):
        print(f"Latitude: {self.sensorDataPack.lat}")
        print(f"Longitude: {self.sensorDataPack.long}")
        print(f"Altitude (GPS): {self.sensorDataPack.alt}")
        print(f"Temperature: {self.sensorDataPack.temperature}")
        print(f"Pressure: {self.sensorDataPack.pressure}")
        print(f"Altitude (BME): {self.sensorDataPack.altitude}")
        print(f"Voltage: {self.sensorDataPack.voltage}")
        print(f"Roll: {self.sensorDataPack.roll}")
        print(f"Pitch: {self.sensorDataPack.pitch}")
        print(f"Yaw: {self.sensorDataPack.yaw}")
        print(f"Date and Time: {self.sensorDataPack.dateAndTime}")