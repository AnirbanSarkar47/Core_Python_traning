'''
step 1: create an empty dict
|
step 2: file handling - read data from network.cfg file - line by line
     - split each line into multiple values 
     - based on = (ex:  'Type=ethernet'.split("=") ->['Type','ethernet'])
                                    0         1
     - add data to dictionary 
                   ----------
            List of 0th index Key ; List of 1st index Value

step 3: use pprint.pprint(dict_Data) - display network data
|
step 4: dict operation
|
step 5: use pprint.pprint(updated_data) - display updated dict 
|
step 6: file handling - create a newConfig file - write updated dict contents to newFile
            (same network config format)
------------------------------------------------------------------------------------
'''



import pprint
import os
import sys
import importlib







import pprint


network_params = {} # empty dict


with open('network.cfg','r') as fobj:
    for var in fobj.readlines():
        var = var.strip() # remove \n
        K,V = var.split("=")
        network_params[K] = V # adding new data to dict
        
        
pprint.pprint(network_params)


network_params['Interface'] = 'eth1'
network_params['bootproto'] = 'static'
network_params['onboot'] = 'yes'
network_params['IPADD'] = '192.168.1.10'
network_params['PREFIX'] = 24
network_params['DNS1']= '122.33.344.555'


print('\nUpdated Dict details:-')
pprint.pprint(network_params)


with open('new_network.cfg','w') as wobj:
    for var in network_params:
        wobj.write(f'{var} = {network_params.get(var)}\n')
