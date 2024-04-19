from ipaddress import *

for mask in range(33):
    net = ip_network(f"127.254.123.15/{mask}", False)  # False если на основе ip адреса
    print(net,net.netmask)
