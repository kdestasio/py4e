# Compare to xml_loop_through_nodes.py for the XML version of this same loop

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(data) # json.loads returns a python list
print('User count:', len(info))

for item in info: # Each item is a python dictionary
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# Code: http://www.py4e.com/code3/json2.py