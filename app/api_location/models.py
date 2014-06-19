

class GPSData:
    
    def fromRequest(self, gpsfix ):
        latitude = gpsfix['latitude']
        longitude = gpsfix['longitude']
        time = gpsfix['time']
        altitude = gpsfix['altitude']
        eps = gpsfix['eps']
        epx = gpsfix['epx']
        epv = gpsfix['epv']
        ept = gpsfix['ept']
        speed = gpsfix['speed']
        climb = gpsfix['climb']
        track = gpsfix['track']
        mode = gpsfix['mode']
