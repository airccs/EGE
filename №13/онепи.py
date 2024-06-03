from ipaddress import *
net = ip_network(f"112.208.0.0/255.255.128.0", 0)
k = 0

for ip in net:
    ip_2 = f"{ip:b}"
    s = ip_2.count("1")
    if s % 11 == 0:
        k += 1
print(k)