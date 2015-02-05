# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth

import xml.etree.ElementTree as etree


def xml_depth(root):
    return max([0] + [xml_depth(child) + 1 for child in root])

N = input()
xmlstring = '\n'.join([raw_input() for _ in xrange(N)])

tree = etree.ElementTree(etree.fromstring(xmlstring))

print xml_depth(tree.getroot())
