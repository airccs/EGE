from ipaddress import *

for i in range(9):
    a = "1" * i + "0" * 8
    a = int(a[:8], 2)
    ip_net = ip_network(f"255.201.33.160/255.255.{a}.0", False)  # False если на основе ip адреса
    for ip_add in ip_net:
        if (bin(int(ip_add))[:-16].count("1") >= bin(int(ip_add))[-16:].count("1")) == False:
            break
    else:
        print(a)
