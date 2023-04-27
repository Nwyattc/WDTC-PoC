#!/usr/bin/env python3

from netmiko import ConnectHandler

def conf_ospf():
    listip = ['1.1.255.5', '1.1.255.6', '1.1.255.2']
    rname = ['R5', 'R6', 'R2']

    for ipadd,r in zip(listip,rname):
        routers = {
        "device_type": "cisco_ios",
        "ip": ipadd,
        "username": "wdtc",
        "password": "wdtc",
        "secret": "wdtc",
        }

        with ConnectHandler(**routers) as konnect:
#            if not konnect.check_enable_mode():
                konnect.enable()
                print("Successfully logged in "+r)

                fp = "/etc/ansible/"+r+".txt"
                konnect.config_mode()
                res = konnect.send_config_from_file(config_file=fp)
                print(res)

def main():
    conf_ospf()

if __name__ == '__main__':
    main()
#    conf_ospf()
