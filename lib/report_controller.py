from collections import OrderedDict
from collections import defaultdict

class ReportController(object):
    def __init__(self):
        self.other_country = defaultdict(list)
        self.usa = defaultdict(list)

    def build_dictionary(self, country_name, state, request_m):
        if country_name == "United States":
            return self.usa[state].append(request_m)
        return self.other_country[country_name].append(request_m)

    def find_most_visited_sites(self, request_list):
        cnt = Counter(request_list)
        top_2 = cnt.most_common(2)

        if top_2[0][0] == "/":
            return top_2[1][0]
        return top_2[0][0]

    def calculate_top_10(self, r_type):
        if r_type == "country":
            modified_dict = OrderedDict(sorted(self.other_country.items(), key=lambda item: len(item[1]), reverse=True)[:10])
        else:
            modified_dict = OrderedDict(sorted(self.usa.items(), key=lambda item: len(item[1]), reverse=True)[:10])

        for k, v in modified_dict.iteritems():
            modified_dict[k] = (len(v), self.find_most_visited_sites(v))
        return modified_dict

    def report(self, r_type):
        result = ""
        if r_type == "country":
            data = self.calculate_top_10("country")
        else:
            data = self.calculate_top_10("usa")

        for k, v in data.iteritems():
            result += "location: %s \t\t total visits:%s \t\t most visited site: %s \n" % (k, v[0], v[1])
        return result
