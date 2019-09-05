
# 方法一:
import socket
import struct
def ip2long(ipstr):
    return struct.unpack("!I", socket.inet_aton(ipstr))[0]

def long2ip(ip):
    return socket.inet_ntoa(struct.pack("!I", ip))
input_Ip = '172.25.254.2'
start_Ip = '172.25.254.15'
end_Ip = '172.25.254.3'
print(ip2long(start_Ip) < ip2long(input_Ip) < ip2long(end_Ip))

# 方法二:
from IPy import  IP
print(IP(start_Ip) < IP(input_Ip) < IP(end_Ip))