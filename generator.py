#!/usr/bin/env python
import os
import sys
from random import randint


files = sys.argv[1:]
path = files[0]
print("Working on Building log file for 2014-10-31")
def ipPool(i):
    ip=["192","168","0",1]
    if i>255:
        ip=["192","168",i//255,1]
        i = i%255
        ip[2]=str(ip[2])
    ip[3]+= i
    ip[3]=str(ip[3])
    return (".".join(ip))

with open (path,"a+") as f:
    for i in range(1414713600,1414800000,60):
        for j in range(1000):
            for k in range(2):
                f.write('{}:{}:{}:{}\n'.format(i,ipPool(j),k, randint(0, 100)))
                # f.write("\n")


print("File Created at {}".format(os.path.realpath(path)))