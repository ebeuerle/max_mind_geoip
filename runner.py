import lib
from clfparser import CLFParser


class GeoIP_apache():
    def __init__(self):
        self.file = lib.FileController()
        self.geoip_data = lib.GeoIPController()
        self.sanity = lib.Sanity()
        #sys.tracebacklimit = 0

    def run(self):
        geo = dict()
        self.apache_file = self.file.read_file()
        for line in self.apache_file:
            clfParts = CLFParser.logParts(line,'%h %r')
            if self.sanity.match_regex(clfParts[1]):
                pass
            else:
                self.resp = self.geoip_data.query_geoip_db(clfParts[0])
                geo[clfParts[0]] = {'country' : self.resp.country.name, 'state' : self.resp.subdivisions.most_specific.name}
                print self.resp.country.name, self.resp.subdivisions.most_specific.name

def main():
    #sys.stdout = lib.Logger(logging.info)
    #sys.stderr = lib.Logger(logging.warning)
    top_geoip_apache = GeoIP_apache()
    top_geoip_apache.run()

if __name__ == "__main__":
    main()
