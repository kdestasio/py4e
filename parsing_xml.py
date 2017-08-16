# XML - eXtensible Markup Language

import xml.etree.ElelmentTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) # If this line of code succeedes, the xml is good
print('Name:',tree.find('name').text) # Within that xml, go find the tag 'name'; text is an attribute of the name node
print('Attr:',tree.find('email').ger('hide')) # Find the email tag and find the 'hide' attribute within the tag email (will return "yes")

# Code: http://www.py4e.com/code3/xml1.py