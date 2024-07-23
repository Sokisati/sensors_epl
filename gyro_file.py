import time
import math
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

class MPUSensor:
    def __init__(self, dt=1.0):
        self.dt = dt  
        self.yaw = 0  
        self.gyroZBias = 0  

        self.mpu = MPU9250(
            address_ak=AK8963_ADDRESS,
            address_mpu_master=MPU9050_ADDRESS_68,
            address_mpu_slave=None,
            bus=1,
            gfs=GFS_250, 
            afs=AFS_2G,  
            mfs=AK8963_BIT_16,  
            mode=AK8963_MODE_C100HZ 
        )
        time.sleep(0.4)
        self.mpu.configure()
        time.sleep(0.4)
        self.calculateGyroBias()

    def calculateGyroBias(self):
        biasSum = 0
        numSamples = 100  
        for _ in range(numSamples):
            gyroData = self.mpu.readGyroscopeMaster()
            biasSum += gyroData[2]  
            time.sleep(0.01)
        self.gyroZBias = biasSum / numSamples

    def getRoll(self):
        accelData = self.mpu.readAccelerometerMaster()
        ax, ay, az = accelData
        roll = math.atan2(ay, az) * (180 / math.pi)
        return roll

    def getPitch(self):
        accelData = self.mpu.readAccelerometerMaster()
        ax, ay, az = accelData
        pitch = math.atan2(-ax, math.sqrt(ay * ay + az * az)) * (180 / math.pi)
        return pitch

    def getYaw(self):
        gyroData = self.mpu.readGyroscopeMaster()
        gyroZ = gyroData[2]
        self.yaw += (gyroZ - self.gyroZBias) * self.dt
        return self.yaw
    
    def test(self,forNumber):
        for i in range(forNumber):
            print("Roll");
            print(self.getRoll);
            print("Pitch");
            print(self.getPitch);
            print("Yaw");
            print(self.getYaw);
        
