"""from ipaddress import *

k = 0
for n in range(0,9):
    A = int("1" * n + "0" * (8 - n),2)
    net = ip_network(f"255.224.33.160/255.255.{A}.0", False)
    for i in net:
        if (f"{i:b}"[:16].count("1") >= f"{i:b}"[16:].count("1")) == False:
            break
    else:
        print(A)"""
from ipaddress import *

k = 0
for A in range(0,256):
    net = ip_network(f"127.254.{A}.19/255.255.224.0", False)
    for i in net:
        if (f"{i:b}"[:16].count("1") >= f"{i:b}"[16:].count("1")) == False:
            break
    else:
        print(A)