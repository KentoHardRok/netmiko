#!/usr/bin/python3
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler

#### Defining Lab Credentials ####

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.101',
    'username': 'tomw',
    'password': 'mR7h0M@$',
}

device = ConnectHandler(**R1)

print(device.send_command('show ip int br'))

config_command = (
    'int lo1',
    'desc Test Loopback',
    'ip add 1.1.1.2 255.255.255.255',
    'do wr',
    )
print(device.send_config_set(config_command))

device.disconnect()


