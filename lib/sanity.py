import sys
import re

class Sanity(object):

    def match_regex(self, request):
        regexList = [
          "[a-f0-9]+/css",
          "[a-f0-9]+/images",
          "[a-f0-9]+/js",
          "entry-images",
          "images",
          "user-images",
          "static",
          "robots.txt",
          "favicon.ico"
          ".rss$",
          ".atom$"
        ]
        gotMatch = False
        for regex in regexList:
            match = re.search(regex,line)
            if match:
                gotMatch = True
                break

        if gotMatch:
            return match
