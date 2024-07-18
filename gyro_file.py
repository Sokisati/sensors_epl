from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import time
import math

class MPUSensor:
    def __init__(self, addressAk=AK8963_ADDRESS, addressMpuMaster=MPU9050_ADDRESS_68, bus=1, gfs=GFS_250, afs=AFS_2G, mfs=AK8963_BIT_16, mode=AK8963_MODE_C100HZ):
        self.mpu = MPU9250(
            address_ak=addressAk,
            address_mpu_master=addressMpuMaster,
            address_mpu_slave=None,
            bus=bus,
            gfs=gfs,
            afs=afs,
            mfs=mfs,
            mode=mode
        )
        self.mpu.calibrateMPU6500()
        self.mpu.configureMPU6500()
        self.mpu.configureAK8963()

    def readAccelerometer(self):
        return self.mpu.readAccelerometerMaster()

    def calculateAngles(self, accelData):
        ax, ay, az = accelData
        pitch = math.atan2(ay, math.sqrt(ax * ax + az * az)) * 180.0 / math.pi
        roll = math.atan2(-ax, math.sqrt(ay * ay + az * az)) * 180.0 / math.pi
        yaw = math.atan2(math.sqrt(ax * ax + ay * ay), az) * 180.0 / math.pi
        return pitch, roll, yaw

    def getPitch(self):
        accelData = self.readAccelerometer()
        pitch, _, _ = self.calculateAngles(accelData)
        return pitch

    def getRoll(self):
        accelData = self.readAccelerometer()
        _, roll, _ = self.calculateAngles(accelData)
        return roll

    def getYaw(self):
        accelData = self.readAccelerometer()
        _, _, yaw = self.calculateAngles(accelData)
        return yaw


