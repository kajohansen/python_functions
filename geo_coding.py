# -*- coding: utf-8 -*- 
#!/usr/bin/python
#
# Geo Coding
import sys

def LatLngToDecimal(deg, mins, sec, cardinal):
    decimal_min = mins / 60.0
    decimal_sec = float(sec) / 3600
    decimal = deg + decimal_min + decimal_sec
    cardinal = cardinal.upper()
    if (cardinal == "N"):
        print str(decimal) + " North"
    elif (cardinal == "S"):
        print "-" + str(decimal) + " South"
    elif (cardinal == "E"):
        print str(decimal) + " East"
    elif (cardinal == "W"):
        print "-" + str(decimal) + " West"
    else:
        print "Error"
        
def DecimalToLatLng(decimal_deg, lat_lng):
    lat_lng = lat_lng.lower()
    decimal_deg_str = str(decimal_deg)
    # we extract the degree decimal by splitting the decimal_degree string
    degrees_array = decimal_deg_str.split(".", 2)
    degrees = degrees_array[0]
    decimal = degrees_array[1]
    # we multiply the decimal minute by sixty and extract the whole number
    decimal_minute = "0." + decimal
    min_sixty = float(decimal_minute) * 60
    minutes = int(min_sixty)
    
    decimal_array = str(min_sixty).split(".", 2)
    decimal_second = "0." + decimal_array[1]
    sec_sixty = float(decimal_second) * 60
    seconds = str(sec_sixty)[0:5]
    # find out if we are returning latitude or longitude
    if (lat_lng == "lat"):
        lat_lng = "Lat: "
        if (decimal_deg_str[0:1] == "-"):
            cardinal = "S"
        else:
            cardinal = "N"
    elif (lat_lng == "lng"):
        lat_lng = "Lng: "
        if (decimal_deg_str[0:1] == "-"):
            cardinal = "W"
        else:
            cardinal = "E"
    # print the coordinates
    print lat_lng + " " + degrees + u"° " + str(minutes) + "' " + str(seconds) + "' " + cardinal

# get the command line arguments
if (len(sys.argv) == 5):
    deg = sys.argv[1]
    mins = sys.argv[2]
    sec = sys.argv[3]
    cardinal = sys.argv[4]
    LatLngToDecimal(float(deg), float(mins), float(sec), str(cardinal)) 
elif (len(sys.argv) == 3):
    deg = sys.argv[1]
    lat_lng = sys.argv[2]
    DecimalToLatLng(float(deg), str(lat_lng))
else:
  print "You can either put decimal latitude or longitude"
  print " -- example1: 51.17926388888888 Lat"
  print " -- example2: -1.8262 Lng"
  print "-- Or --"
  print "You can put degrees minutes seconds and cardinal direction"
  print " -- example: 19 18 6 n"
    
# LatLngToDecimal(19, 18, 6, "n")
# LatLngToDecimal(51, 10, 45.35, "s")
# DecimalToLatLng(51.17926388888888, "LAt")
# DecimalToLatLng(-1.8262166666666666, "Lng")
