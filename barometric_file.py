import time
import bme680

class BMESensor:
    def __init__(self):
        try:
            self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
        except (RuntimeError, IOError):
            self.sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

        self.sensor.set_humidity_oversample(bme680.OS_2X)
        self.sensor.set_pressure_oversample(bme680.OS_4X)
        self.sensor.set_temperature_oversample(bme680.OS_8X)
        self.sensor.set_filter(bme680.FILTER_SIZE_3)
        # Disable gas measurements
        self.sensor.set_gas_status(bme680.DISABLE_GAS_MEAS)

        self.temperature = None
        self.pressure = None
        self.humidity = None
        self.altitude = None

    def readSensorData(self):
        if self.sensor.get_sensor_data():
            self.temperature = self.sensor.data.temperature
            self.pressure = self.sensor.data.pressure * 100  
            self.humidity = self.sensor.data.humidity
            self.altitude = 44330 * (1 - (self.pressure / 101325) ** (1 / 5.255)) 
            return True
        return False

    def getTemp(self):
        return self.sensor.data.temperature

    def getPressure(self):
        return self.sensor.data.pressure * 100 

    def getAlt(self):
        pressure = self.getPressure();
        return (44330 * (1 - (pressure / 101325) ** (1 / 5.255)))
    
    def test(self):
        if self.sensor.get_sensor_data():
            print("temp:")
            print(self.getTemp());
            print("pressure:")
            print(self.getPressure());
            print("alt:")
            print(self.getAlt());
        else:
            print("error")

