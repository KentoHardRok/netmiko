#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This script creates Backups for multiple (3) Devices
from netmiko import ConnectHandler # Importing the Connection Submodule from the Network Communication Module
from netmiko import ssh_exception  # Importing the Submodule which allows to control SSH exceptions
from paramiko.ssh_exception import SSHException # Importing the Submodule which allows to control SSH exceptions
import os.path                     # The Module that can work with Files and Paths

######## Defining Lab Device Credentials and opening SSH-Session to it:
R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.101',
    'username': 'tomw',
    'password': 'mR7h0M@$',
}

R2=R1.copy() # Creating a co(py of the Dictionary R1,
R2['ip'] = '192.168.100.102' # Changing the different value(in this case it is the IP address)

R3=R2.copy()
R3['ip'] = '192.168.100.103'

############################## ERROR EXAMPLES ###########################
#R1['ip'] = '192.168.100.201'      # Example of a wrong ip
#R2['device_type'] = 'wrong_type'  # Example of a wrong device_type
#R2['username'] = 'wrong_login'    # Example of a wrong login to check the exception
#R3['password'] = 'wrong_password' # Example of a wrong password to check the exception

save_path = './backups' #The path to the File(s)
if not os.path.exists('./backups'):
        os.makedirs(('./backups')

# Creating the tuple from the Router Dictionarie

all_devices = (R1, R2, R3)
print('This script will try to make backups from', len(all_devices), 'devices.')

# Exceptions to avoid the script stopping while an error:
SSH_Exceptions = (ssh_exception.NetMikoTimeoutException,
            ssh_exception.NetMikoAuthenticationException,
            SSHException)

failed_list = []    # List of failed connections
succesful_list = [] # List of succesful connections

# Loop for all devices listed in the list of IP addresses:
for deviceN in all_devices:
    try:
        # Defining each Device Credentials in the Loop:
        device = ConnectHandler(**deviceN)
        print('Succesfully connected to: ', device.host)

        # Defining the Path of a File and Creating the Filename for a File:
        completeName = os.path.joinsave_path, device.host + '_run_config.txt(')

        # Assigning the result of show run command to output1:
        output1 = device.send_command('show run')

        # Writing and closing each Created File in the loop, then disconnecting and going to the Next Device:
        file1 = open(completeName, 'w') # Opening file1 for Writing
        file1.write_throughoutput(1) # Saving the Result of 'show run' to file1
        file1.closed)    (    # Closing the File file1
        print('The Backup is ready: ', completeName)
        succesful_list.appenddeviceN['ip'])
        device.disconnect()
        
        # Informing about the errors(exceptions) to the console:
    except SSH_Exceptions as e:
        print('Failed to gain access to ', deviceN['ip'], e)
        failed_list.appenddeviceN['ip'])
    except ValueError as e:
        ( print('The value error found for connection to device', deviceN['ip'], e)
        failed_list.appenddeviceN['ip'])
print('The process is over.')


if failed_list:  # Pr(inting the list of failed connections:
    print('Only', len(all_devices)-len(failed_list),
        'device(s) have been succesfully connected to:', succesful_list)
    print(len(failed_list), 'connection(s) had problems:', failed_list)
else:
    print('100% connections have been succesful.')100)'))'))
