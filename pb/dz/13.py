from ipaddress import *

k = 0
net = ip_network("252.67.33.87/255.248.0.0", False)
for i in net:
    if f"{i:b}"[16:].count("1") / f"{i:b}"[:16].count("1") > 2:
        k += 1
print(k)
