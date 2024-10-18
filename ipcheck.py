import ipaddress as ipaddr
from pprint import pprint
x = list(ipaddr.ip_network("192.168.52.0/28",False))
pprint(x)
