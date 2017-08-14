import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import string

OSMFILE = "C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\Portland.osm"
phone_type = re.compile(r'\+1\-\d{3}\-\d{3}\-\d{4}')  #Required format: "+1-###-###-####"

def audit_phone_type(phone_types, phone_number):
    m = phone_type.search(phone_number)
    if m is None:
        phone_types[phone_type].add(phone_number)

def is_phone_number(elem):
    return (elem.attrib['k'] == "phone")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    phone_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_phone_number(tag):
                    audit_phone_type(phone_types, tag.attrib['v'])
    osm_file.close()
    return phone_types

def test():
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))


if __name__ == '__main__':
    test()