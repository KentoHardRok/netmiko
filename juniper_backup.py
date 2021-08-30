#!/usr/bin/python3
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
from colorama import Fore, Style
import os.path

num_of_dev = 5
dev_proname = "R"
dev_list = {}
hostnet = "192.168.100.110"


def ipinc(ip, n):
    ip_list = []
    octets = ip.split(".")
    int_octets = list(map(int, octets))
    for i in range(n):
        int_octets[3] += 1
        ip_list.append('.'.join(list((map(str, int_octets)))))
    return (ip_list)


net = ipinc(hostnet, num_of_dev)

for i in range(num_of_dev):
    dev_list[f'{dev_proname}{i+1}'] = {
        'device_type': 'juniper',
        'ip': net[i],
        'username': 'tomw',
        'password': 'mR7h0M@$',
    }

save_path = './backups'  #Path to files
if not os.path.exists('./backups'):
    os.makedirs('./backups')
for router in dev_list.values():
    print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
    with ConnectHandler(**router) as device:
        # Defining the Path of a File and Creating the Filename for a File
        completeName = os.path.join(save_path, device.host + '_run_config.txt')
        # Assigning the Result of show run to output1
        output1 = device.send_command('show config')
        file1 = open(completeName, 'w')
        file1.write(output1)
        file1.close()
        print(device.host, "has completed")
