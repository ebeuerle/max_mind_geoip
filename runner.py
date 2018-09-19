import lib
from clfparser import CLFParser
from collections import OrderedDict
from collections import defaultdict
class GeoIP_apache():
    def __init__(self):
        self.file = lib.FileController()
        self.geoip_data = lib.GeoIPController()
        self.sanity = lib.Sanity()
        self.other_country = defaultdict(list)
        self.usa = defaultdict(list)
        #sys.tracebacklimit = 0

    def build_dictionary(self, country_name, state, request_m):
        if country_name == "United States":
            return self.usa[state].append(request_m)
        return self.other_country[country_name].append(request_m)

    def calculate_top_10(self, r_type):
        if r_type == "country":
            modified_dict = OrderedDict(sorted(self.other_country.items(), key=lambda item: len(item[1]), reverse=True)[:10])
        else:
            modified_dict = OrderedDict(sorted(self.usa.items(), key=lambda item: len(item[1]), reverse=True)[:10])

        for k, v in modified_dict.iteritems():
            modified_dict[k] = (len(v), max(v,key=v.count))
        return modified_dict

    def report(self, r_type):
        result = ""
        if r_type == "country":
            data = self.calculate_top_10("country")
        else:
            data = self.calculate_top_10("usa")

        for k, v in data.iteritems():
            result += "location: %s \t\t total visits:%s \t\t most visited site: %s" % (k, v[0], v[1])
        return result

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
                self.build_dictionary(resp.country.name, resp.subdivisions.most_specific.name, clfParts[1])
        print self.report("country")
        print self.report("usa")

def main():
    #sys.stdout = lib.Logger(logging.info)
    #sys.stderr = lib.Logger(logging.warning)
    top_geoip_apache = GeoIP_apache()
    top_geoip_apache.run()

if __name__ == "__main__":
    main()
