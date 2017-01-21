#!/usr/bin/env python3

import argparse, ipaddress, socket, geoip2.database
input = argparse.ArgumentParser()
input.add_argument("host", type=str, help="enter the host to locate")
input_args = input.parse_args()

ip_reader = geoip2.database.Reader('/volumes/files/personal/utilities/network/dependencies/GeoLite2-City.mmdb')

def input_validate(host):
    try:
        ipaddress.ip_address(host)
        return host
    except:
        output = socket.gethostbyname(host)
        print("Converted {0} to {1}".format(host, output))
        print("------------")
        return output

def ip_locate(host):
    hostname = input_validate(host)
    resp = ip_reader.city(hostname)
    lat = str(resp.location.latitude)
    long = str(resp.location.longitude)
    print("The host is located in {0}, {1}, in {2}".format(resp.city.name, resp.subdivisions.most_specific.iso_code, resp.country.name))
    print("------------")
    print("Latitude: {0}, Longitude: {1}".format(lat, long))

if __name__ == '__main__':
    ip_locate(input_args.host)
