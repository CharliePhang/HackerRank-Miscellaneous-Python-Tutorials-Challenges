# https://www.hackerrank.com/challenges/xml-1-find-the-score

N = input()

xmlstring = '\n'.join([raw_input() for _ in xrange(N)])
# print xmlstring

import xml.etree.ElementTree as etree

tree = etree.ElementTree(etree.fromstring(xmlstring))
print tree.iter()
#root = tree.getroot()

xml_score = 0
for element in tree.iter():
    print element.attrib
    xml_score += len(element.attrib)

print xml_score