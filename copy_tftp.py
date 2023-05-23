#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException
from netmiko import NetmikoAuthenticationException
import time

username = input('Enter username: ')
password = getpass()

#with open('commands_file.txt') as f:
    #commands_list = f.read().splitlines()

with open('devices.txt') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print('Connecting to device: ' + devices)
    ip_address_of_device = devices
    router = {
        'device_type': 'cisco_ios_telnet',
        'ip': ip_address_of_device,
        'username': username,
        'password': password,
    }

    try:
        net_connect = ConnectHandler(**router)
        #time.sleep(1)
    except (NetmikoAuthenticationException):
        print('Authentication failure:' +  ip_address_of_device )
        continue
    except (NetMikoTimeoutException):
        print('Timeout to device: ' + ip_address_of_device)
        continue
    except (EOFError):
        print('End of file while attempting device ' + ip_address_of_device)
        continue
    except Exception as unknown_error:
        print('Some other error: ' + ip_address_of_device + ':' + str(unknown_error))
        continue
    time.sleep(5)

    output = net_connect.send_command_timing('copy tftp://192.168.122.71/test3.txt flash:')
    if 'Destination filename' in output:
        output += net_connect.send_command_timing('\n')
        if 'Do you want to over' in output:
            output += net_connect.send_command_timing('\n')
    #print(output)
    saveoutput =  open('output.txt', 'a')
    saveoutput.write('\nDevice_' + ip_address_of_device)
    saveoutput.write('\n')
    saveoutput.write(output)
    saveoutput.write('\n#########################')
    saveoutput.write('\n')
    saveoutput.close()
