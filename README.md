# MaxMind GeoIP script

Version: *1.0*
Author: *Eddie Beuerlein*

### Summary
Script iterates through Apache log file, then looks up the IP addresses in GeoIP database.  It then prints out a top 10 break down report for countries and US states.

### Requirements and Dependencies

1. Python 2.7.10 or newer (not Python 3.x)

2. CLFParser

```
pip install cflparser

```
3. GeoIP2 APIs
```
pip install geoip2
```
4. Download the Geo City database from below (untar and ungzip it in the main directory where runner.py is located.
```
http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
```

### Configuration

1. Navigate to */configs/configs.yml*
2. Add the GeoIP database directory (since it can change when database releases) to the yaml file.  This will dictate the directory it will use to access the database.
3. Put your Apache access.log file in the same directory as runner.py as well.


### Run

```
python runner.py

```
