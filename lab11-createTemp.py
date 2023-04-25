#! /usr/bin/env python3

from netmiko import ConnectHandler
import csv
import yaml

def get_routerinfo():
    loopbacks = ""
    phyint = ""
    ospf = ""
    dict1 = {}
    final="---\nrouters:"
    with open('lab11-router_ospf.csv', 'r') as f:
        data = csv.DictReader(f)
        for r in data:
            hname = r["hostname"]
            if hname not in dict1 and r["interface"] != 'NA':
                dict1[hname] = 'yes'
                final+=loopbacks
                final+=phyint
                final+=ospf
                final+= "\n  - hostname: "+hname
                loopbacks="\n    loopbacks:"
                phyint="\n    interfaces:"
                ospf="\n    ospf:\n      - process: "+r["process"]
                ospf+="\n        networks: "
                #bgp="\n    bgp:\n      - as: "+r["process"]

            if r["interface"].startswith("Loopback"):
                loopbacks+="\n      - name: "+r["interface"]
                loopbacks+="\n        ip: "+r["ip"]
                # ospf+="\n        networks: "
                ospf+="\n          - network "+r["networks"]+" "+r["wildc"]+" area "+r["area"]
            else:
                phyint+="\n        "+r["interface"]+": "+r["ip"]
                ospf+="\n          - network "+r["networks"]+" "+r["wildc"]+" area "+r["area"]

    final+=loopbacks
    final+=phyint
    final+=ospf
    print(final)

    fp = "/etc/ansible/roles/routers/vars/main.yml"
    with open(fp, 'w') as file:
        file.write(final)

get_routerinfo()
