import gps
import time

class GPSSensor:
    def __init__(self):

        self.session = gps.gps(mode=gps.WATCH_ENABLE)
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        time.sleep(1);
    
    def getLat(self):
        report = self.session.next()
        while report['class'] != 'TPV':
            report = self.session.next()
        return report.lat

    def getLong(self):
        report = self.session.next()
        while report['class'] != 'TPV':
            report = self.session.next()
        return report.lon

    def getAlt(self):
        report = self.session.next()
        while report['class'] != 'TPV':
            report = self.session.next()
        return report.alt

    def test(self):
        print("Latitude:", self.getLat())
        print("Longitude:", self.getLong())
        print("Altitude:", self.getAlt())

