#! /usr/bin/env python3

from easysnmp import Session, snmp_walk
import time
import matplotlib.pyplot as plt
import json

def cpu_graph():
    util = []
    ti = 0
    time1 = []

    t = time.time() + 30
    while time.time() < t:
        cpu = snmp_walk('1.3.6.1.4.1.9.2.1.56', hostname= '1.1.255.5', community='wdtc', version=2)
        for i in cpu:
            p = int(i.value)
            util.append(p)
            ti = ti + 5
            time1.append(ti)
        time.sleep(5)
    #print(time1)
    util1 = list(map(int, util))
    #print(util1)
    plt.plot(time1, util1, label = 'CPU Utilization')
    plt.xlabel('Time')
    plt.ylabel('Percentage')
    plt.legend()
    plt.savefig("Utilization.jpg")
    print("CPU Utilization graph captured.")

cpu_graph()
