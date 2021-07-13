#!/usr/bin/python3
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler  # import connection handler module in python
import os.path                      # Module to work with file paths

#### Defining Lab Credentials ####

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.101',
    'username': 'tomw',
    'password': 'mR7h0M@$',
}

device = ConnectHandler(**R1)

save_path = './backups' #Path to files
if not os.path.exists('./backups'):
    os.makedirs('./backups')

# Defining the Path of a File and Creating the Filename for a File
completeName = os.path.join(save_path, device.host + '_run_config.txt')

# Assigning the Result of show run to output1
output1 = device.send_command('show run')

file1 = open(completeName, 'w')
file1.write(output1)
file1.close()

device.disconnect()

