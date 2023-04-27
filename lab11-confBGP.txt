#!/usr/bin/env python3

from netmiko import ConnectHandler
import csv

def configure_intf():
    with open('router_bgp.csv', 'r') as file:
        data = csv.DictReader(file)
        for i in data:
            routers = {
            "device_type": "cisco_ios",
            "ip": i["mgmt"],
            "username": i["user"],
            "password": i["pass"]
            }
            with ConnectHandler(**routers) as konnect:
                #if not konnect.check_enable_mode():
                    #konnect.enable()
                    print("Logged in to {}".format(i["hostname"]))
                    if i["interface"].startswith("Loopback"):
                        intf= konnect.send_config_set(['int {}'.format(i["interface"]), 'ip addr {}'.format(i["ip"])])
                        print(intf)
                    else:
                        intf= konnect.send_config_set(['int {}'.format(i["interface"]), 'ip addr {}'.format(i["ip"]), 'no shut'])
                        print(intf)

def configure_bgp():
    with open('router_bgp.csv', 'r') as file:
        data = csv.DictReader(file)
        for i in data:
            routers = {
            "device_type": "cisco_ios",
            "ip": i["mgmt"],
            "username": i["user"],
            "password": i["pass"]
            }
            with ConnectHandler(**routers) as konnect:
                #if not konnect.check_enable_mode():
                    #konnect.enable()
                    print("Logged in to {}".format(i["hostname"]))
                    if i["interface"].startswith("Loopback"):
                        bgpconf = konnect.send_config_set(['router bgp {}'.format(i["as"]), 'neighbor {0} remote-as {1}'.format(i["nip"],i["as"]), 'neighbor {} update-source Loopback 1'.format(i["nip"]), 'neighbor {} next-hop-self'.format(i["nip"])])
                        print(bgpconf)
                    else:
                        bgpconf = konnect.send_config_set(['router bgp {}'.format(i["as"]), 'neighbor {0} remote-as {1}'.format(i["nip"],i["nas"]),'neighbor {} next-hop-self'.format(i["nip"])])
                        print(bgpconf)

configure_intf()
configure_bgp()
