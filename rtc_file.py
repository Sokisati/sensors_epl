import time
import board
import busio
import adafruit_ds1307

class RTCSensor:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.rtc = adafruit_ds1307.DS1307(self.i2c)
        self.ensureRtcIsRunning()

    def ensureRtcIsRunning(self):
        if not self.rtc.datetime:
            print("RTC is not running. Setting the time...")
            self.rtc.datetime = time.struct_time((2024, 7, 8, 12, 0, 0, 0, -1, -1))
    
    def getDateAndTime(self):
        current_time = self.rtc.datetime
    
        formatted_time = "{:02d}/{:02d}/{:04d},{:02d}/{:02d}/{:02d}".format(
            current_time.tm_mday,
            current_time.tm_mon,
            current_time.tm_year,
            current_time.tm_hour,
            current_time.tm_min,
            current_time.tm_sec
        )
        return formatted_time
    
    def test(self):
        time = self.getDateAndTime();
        print(time);

