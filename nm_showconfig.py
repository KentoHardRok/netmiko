#!/usr/bin/python3
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
from colorama import Fore, Style

ip_list = []
for host in range(101, 109):
    dev_ip='192.168.100.{}'.format(host)
    ip_list.append(dev_ip)

command_output=''

for num in range(len(ip_list)):
    device = ConnectHandler(device_type='cisco_ios', ip=ip_list[num], username='tomw', password='mR7h0M@$')
    command_output += device.send_command('show run | inc hostname')
    command_output += ("\n\n")
    command_output += device.send_command('show ip int br')
    command_output += ("\n" + Fore.YELLOW + "#" * 70 + Style.RESET_ALL + "\n")

print(command_output)
device.disconnect()
