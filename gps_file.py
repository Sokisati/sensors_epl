import gpsd
import time

class GPSSensor:
    def __init__(self):

        gpsd.connect()
        time.sleep(1);
    
    def getLat(self):

        packet = gpsd.get_current()
        return packet.lat

    def getLong(self):

        packet = gpsd.get_current()
        return packet.lon

    def getAlt(self):

        packet = gpsd.get_current()
        return packet.alt

    def test(self):
        print("Latitude:", self.getLat())
        print("Longitude:", self.getLong())
        print("Altitude:", self.getAlt())
