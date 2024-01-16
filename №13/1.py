# print(bin(240))
# print(int("11111011", 2))

from ipaddress import *

ip_net = ip_network("142.108.56.118/255.255.255.240", False)  # False если на основе ip адреса
cnt = 0
for ip_add in ip_net:
    if bin(int(ip_add))[-16:].count("1") > bin(int(ip_add))[:-16].count("1"):
        cnt += 1
print(cnt)