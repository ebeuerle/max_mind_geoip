import geoip2.database
import os
import lib

class GeoIPController(object):
    def __init__(self):
        dbdirpath = lib.CONFIG["database_directory"]
        path_to_db = os.path.join(os.path.dirname(__file__), '../dbdirpath/GeoLite2-City.mmdb')
        dbreader = geoip2.database.Reader(path_to_db)

    def query_geoip_db(self, ip):
        response = dbreader.city(ip)
        return response
