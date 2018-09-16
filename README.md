# MaxMind GeoIP script

Version: *1.0*
Author: *Eddie Beuerlein*

### Summary
Script iterates through Apache log file, then looks up the IP addresses in GeoIP database.

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

### Configuration

1. Navigate to */configs/configs.yml*


### Run

```
python runner.py

```
