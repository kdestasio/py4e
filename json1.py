# JSON - JavaScript Object Notation. A means to serialize data.
# http://www.json.org/
# Not as rich a representation as XML, but simpler and still powerful


import json # The curly brace indicates an object with key:value pairs
data = '''{ 
	"name" : "Chuck",
	"phone" : {
	"type" : "intl",
	"number" : "+1 734 303 4456"
	},
	"email" : {
	"hide" : "yes"
	}
}''' 

info = json.loads(data) #loads means load from string
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])