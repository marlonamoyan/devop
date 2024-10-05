import json
import netmiko
from netmiko import ConnectHandler

#tell python to open the Json file:
with open('configcisco1.json') as config_file:
    config = json.load(config_file)
    
    #Extract json config to python memory:
    device_info = config['device']
    interface_config = config['interface_config']
    new_hostname = config['new_hostname']
    
    #Talk using ssh to cisco:
    net_connect = ConnectHandler(**device_info)
    
    #Start Configuring via enable
    net_connect.enable
    
    #Build the Cisco configuration Via Json:
    commands = [
        f"interface {interface_config['interface']}",
        f"ip address {interface_config['new_ip']} {interface_config['subnet_mask']}",
        "no shutdown",
        "exit",
        f"hostname {new_hostname}"
     ]
        
    #Send config to Cisco Device:
    output = net_connect.send_config_set(commands)
    print(output)
    
    #exit/logout from Cisco:
    net_connect.disconnect        