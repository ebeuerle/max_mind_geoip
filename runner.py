import lib
from clfparser import CLFParser


class GeoIP_apache():
    def __init__(self):
        #config = lib.ConfigHelper()
        self.file = lib.FileController()
        #sys.tracebacklimit = 0

    def run(self):
        self.apache_line = self.file.read_file()
        clfParts = CLFParser.logParts(apache_line,'%h %r')
        print clfParts

def main():
    #sys.stdout = lib.Logger(logging.info)
    #sys.stderr = lib.Logger(logging.warning)
    top_geoip_apache = GeoIP_apache()
    top_geoip_apache.run()

if __name__ == "__main__":
    main()
