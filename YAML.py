#Python Script that shows how to import YAML
import yaml
#opens the yaml file that looks like this
'''
#This YAML File Contains a list of nodes. You can add or remote items to the list or change the IP address of the nodes.
 -10.101.8.50
 -10.101.8.51
 -10.101.8.52
...
'''
#start of Open command
with open('nodes.yml','r') as file:
#converts yaml to a python dictionary    
    data = yaml.safe_load(file)
nodes = data
print("This is the list of Nodes from your YAML File ")
for node in nodes:
    print(node)

print("This is just printing out the dictionary serialized")
print(nodes)