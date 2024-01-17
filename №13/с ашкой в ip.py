from ipaddress import *

for a in range(256):
    ip_net = ip_network(f"127.254.{a}.15/255.255.224.0", False)  # False если на основе ip адреса
    for ip_add in ip_net:
        if (bin(int(ip_add))[:-16].count("1") >= bin(int(ip_add))[-16:].count("1")) == False:
            break
    else:
        print(a)
