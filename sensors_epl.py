from rtc_file import *
from gyro_file import *

class SensorPack:
    def __init__(self,rtc,gyro):
        self.rtcSensor = RTCSensor();
        self.gyroSensor = MPUSensor();

    def testSensors(self):
        print(self.rtcSensor.getDateAndTime());


rtc = RTCSensor();
gyro = MPUSensor();
sensorPack = SensorPack(rtc,gyro);

while True:
    sensorPack.testSensors();
        