import lib
from clfparser import CLFParser
from collections import defaultdict

class GeoIP_apache():
    def __init__(self):
        self.file = lib.FileController()
        self.geoip_data = lib.GeoIPController()
        self.sanity = lib.Sanity()
        self.build_report = lib.ReportController()
        #sys.tracebacklimit = 0

    def run(self):
        geo = defaultdict(list)
        self.apache_file = self.file.read_file()
        for line in self.apache_file:
            clfParts = CLFParser.logParts(line,'%h %r')
            if self.sanity.match_regex(clfParts[1]):
                pass
            else:
                try:
                    resp = self.geoip_data.query_geoip_db(clfParts[0])
                except:
                    pass
                self.build_report.build_dictionary(resp.country.name, resp.subdivisions.most_specific.name, clfParts[1].split(" ")[1])
        print "Top 10 for visitors"
        print self.build_report.report("country")
        print "Top 10 US states"
        print self.build_report.report("usa")

def main():
    #sys.stdout = lib.Logger(logging.info)
    #sys.stderr = lib.Logger(logging.warning)
    top_geoip_apache = GeoIP_apache()
    top_geoip_apache.run()

if __name__ == "__main__":
    main()
