"""
    Program 5 of Python Exercise - 2
"""

import ntpath
# from xml.dom import minidom
#
# # parse an xml file by name
# file = minidom.parse("dataxmlfile.xml")
#
import xml.etree.ElementTree as ET

tree = ET.parse("dataxmlfile.xml")
root = tree.getroot()

# finding the state tag and their child attributes.
for child in root:
    print({x.tag for x in root.findall(child.tag + "/*")})
#     print(child.tag,child.attrib)
#     for state in root.findall(child.tag):
#         print(state)

# for state in root.findall('template'):
# 	rank = state.find('xpath').items()
# 	name = state.get('id')
# 	print(name, rank[0][1],'||',state.find('xpath').items()[0][1])

# use getElementsByTagName() to get tag
# template = file.getElementsByTagName('template')
# xpath = file.getElementsByTagName('xpath')
# link = file.getElementsByTagName('link')
# script = file.getElementsByTagName('script')

# # all template ids
# print('\nAll template ids :')
# for elem in template:
#     print(elem.attributes['id'].value)
#
# # all xpath expr
# print('\nAll xpath expr :')
# for elem in xpath:
#     print(elem.attributes['expr'].value)
#
# # all link href
# print('\nAll link href :')
# for elem in link:
#     print(ntpath.basename(elem.attributes['href'].value))
#
# # all script src
# print('\nAll script src :')
# for elem in script:
#     print(ntpath.basename(elem.attributes['src'].value))
