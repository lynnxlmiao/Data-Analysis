import csv
import codecs
import pprint
import re
import xml.etree.cElementTree as ET
from collections import defaultdict

import cerberus

import schema

OSMFILE = r"C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\Portland.osm"

NODES_PATH = r"C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\nodes.csv"
NODE_TAGS_PATH = r"C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\nodes_tags.csv"
WAYS_PATH = r"C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\ways.csv"
WAY_NODES_PATH = r"C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\ways_nodes.csv"
WAY_TAGS_PATH = r"C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\ways_tags.csv"

LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

#SCHEMA = schema.schema

SCHEMA = {
    'node': {
        'type': 'dict',
        'schema': {
            'id': {'required': True, 'type': 'integer', 'coerce': int},
            'lat': {'required': True, 'type': 'float', 'coerce': float},
            'lon': {'required': True, 'type': 'float', 'coerce': float},
            'user': {'required': True, 'type': 'string'},
            'uid': {'required': True, 'type': 'integer', 'coerce': int},
            'version': {'required': True, 'type': 'string'},
            'changeset': {'required': True, 'type': 'integer', 'coerce': int},
            'timestamp': {'required': True, 'type': 'string'}
        }
    },
    'node_tags': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'id': {'required': True, 'type': 'integer', 'coerce': int},
                'key': {'required': True, 'type': 'string'},
                'value': {'required': True, 'type': 'string'},
                'type': {'required': True, 'type': 'string'}
            }
        }
    },
    'way': {
        'type': 'dict',
        'schema': {
            'id': {'required': True, 'type': 'integer', 'coerce': int},
            'user': {'required': True, 'type': 'string'},
            'uid': {'required': True, 'type': 'integer', 'coerce': int},
            'version': {'required': True, 'type': 'string'},
            'changeset': {'required': True, 'type': 'integer', 'coerce': int},
            'timestamp': {'required': True, 'type': 'string'}
        }
    },
    'way_nodes': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'id': {'required': True, 'type': 'integer', 'coerce': int},
                'node_id': {'required': True, 'type': 'integer', 'coerce': int},
                'position': {'required': True, 'type': 'integer', 'coerce': int}
            }
        }
    },
    'way_tags': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'id': {'required': True, 'type': 'integer', 'coerce': int},
                'key': {'required': True, 'type': 'string'},
                'value': {'required': True, 'type': 'string'},
                'type': {'required': True, 'type': 'string'}
            }
        }
    }
}

# Make sure the fields order in the csvs matches the column order in the sql table schema
NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']

#OSMFILE = "C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\Portland_sample.osm"


#########################################
# "Fix" abbreviated street names
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
expected = ["Avenue", "Boulevard", "Commons", "Center", "Court", "Circle", "Drive", "Highway", "Lane",
            "Place", "Parkway", "Road", "Square", "Street",  "Trail", 'Trail', "Way"]
#The dictionary mapping the incorrect street names to correct values
mapping = { "Ave": "Avenue",
            "Ave.": "Avenue",
            "Blvd": "Boulevard",
            "Ct": "Court",
            "Ct.": "Court",
            "center": "Center",
            "Dr": "Drive",
            "Dr.": "Drive",
            "Ln": "Lane",
            "Rd": "Road",
            "Rd.": "Road",
            "rd": "Road",
            "road": "Road",
            "St": "Street",
            "St.": "Street",
            "way": "Way",
            "trail": "Trail",
            "W.": "West",
            "W": "West",
            "S.": "South",
            "S": "South",
            "E.": "East",
            "E": "East",
            "N.": "North",
            "N": "North",
            "SW": "Southwest",
            "SE": "Southeast",
            "NW": "Northwest",
            "NE": "Northeast"
            }

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types

def update_name(name, mapping):
    # Fix problematic street name and street direction
    # Called by shape_element()
    name = name.split(" ")
    for word in range(len(name)):
        if name[word] in mapping.keys():
            name[word] = mapping[name[word]]
    name = " ".join(name)
    return name

# Code for checking update_name result
# st_types = audit(OSMFILE)
# for st_types, ways in st_types.iteritems():
# 	for name in ways:
# 		better_name = update_name(name, mapping)
# 		print name, "->", better_name

#########################################
# "Fix" Inconsistent Phone Number
phone_type = re.compile(r'\+1\-\d{3}\-\d{3}\-\d{4}')  #Required format: "+1-###-###-####"

OSMFILEP = "C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\Portland.osm"

def audit_phone_type(phone_types, phone_number):
    m = phone_type.search(phone_number)
    if m is None:
        phone_types[phone_type].add(phone_number)

def is_phone_number(elem):
    return (elem.attrib['k'] == "phone")


def audit_phone(osmfile):
    osm_file = open(osmfile, "r")
    phone_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_phone_number(tag):
                    audit_phone_type(phone_types, tag.attrib['v'])
    osm_file.close()
    return phone_types

def update_phone_num(phone_num):
    # Fix phone number to
    # Called by shape_element()
    m = phone_type.match(phone_num)
    if m is None:
        # Remove all brackets
        if "(" in phone_num or ")" in phone_num:
            phone_num = re.sub("[()]", "", phone_num)
        # Replace all spaces to dashes
        if " " in phone_num or "  " in phone_num:
            phone_num = re.sub("[ ]+(?=\d)", "-", phone_num)
        # Add dashes for 10 straight numbers
        if re.match(r'\d{10}', phone_num) is not None:
            phone_num = phone_num[:3] + "-" + phone_num[3:6] + "-" + phone_num[6:]
        # Add country code
        if re.match(r'\d{3}\-\d{3}\-\d{4}', phone_num) is not None:
            phone_num = "+1" + phone_num
        elif re.match(r'\+01\-\d{3}\-\d{3}\-\d{4}', phone_num) is not None:
            phone_num = "+1" + phone_num[3:]
        elif re.match(r'1\s\d{3}\s\d{3}\s\d{4}', phone_num) is not None:
            phone_num = "+" + phone_num
        # Ignore tag if no area code and local number (<10 digits)
        elif sum(c.isdigit() for c in phone_num) < 10:
            return None

    return phone_num

# Code for checking update_phone_num result
#phone_types = audit_phone(OSMFILEP)

def load_tag_node(element, secondary, default_tag_type):
    #loop and check secondary node 'tag'
    #called by shape_element()
    res = {}
    res['id'] = element.attrib['id']
    if ":" not in secondary.attrib['k']:
        res['key'] = secondary.attrib['k']
        res['type'] = default_tag_type
    else:
        res['key'] = str(secondary.attrib['k'].split(":", 1)[1])
        res['type'] = str(secondary.attrib['k'].split(":", 1)[0])

    #Update key values here
    if is_street_name(secondary):
        street_name = update_name(secondary.attrib['v'], mapping)
        res['value'] = street_name

    elif is_phone_number(secondary):
        phone_num = update_phone_num(secondary.attrib['v'])
        if phone_num is not None:
            res['value'] = phone_num
        else:   # Ignore tag if no area code and local number (<10 digits)
            return None
    else:
        res['value'] = secondary.attrib['v']

    return res

def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS,
                  problem_chars=PROBLEMCHARS, default_tag_type='regular'):
    #Clean and shape node or way XML element to Python dict
    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []  # Handle secondary tags the same way for both node and way elements
    if element.tag == 'node':
        for attrib, value in element.attrib.iteritems():
            if attrib in node_attr_fields:
                node_attribs[attrib] = value

        for secondary in element.iter():
            if secondary.tag == 'tag':
                if problem_chars.match(secondary.attrib['k']) is not None:
                    continue
                else:
                    res = load_tag_node(element, secondary, default_tag_type)
                    if res is not None:
                        tags.append(res)
        return {'node': node_attribs, 'node_tags': tags}

    elif element.tag == 'way':
        for attrib, value in element.attrib.iteritems():
            if attrib in way_attr_fields:
                way_attribs[attrib] = value

                position = 0
        for secondary in element.iter():
            if secondary.tag == 'tag':
                if problem_chars.match(secondary.attrib['k']) is not None:
                    continue
                else:
                    res = load_tag_node(element, secondary, default_tag_type)
                    if res is not None:
                        tags.append(res)
            elif secondary.tag == 'nd':
                resnd = {}
                resnd['id'] = element.attrib['id']
                resnd['node_id'] = secondary.attrib['ref']
                resnd['position'] = position
                position += 1
                way_nodes.append(resnd)
        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}


# ================================================== #
#               Helper Functions                     #
# ================================================== #
def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


def validate_element(element, validator, schema=SCHEMA):
    """Raise ValidationError if element does not match schema"""
    if validator.validate(element, schema) is not True:
        field, errors = next(validator.errors.iteritems())
        message_string = "\nElement of type '{0}' has the following errors:\n{1}"
        error_string = pprint.pformat(errors)

        raise Exception(message_string.format(field, error_string))

class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
            k: (v.encode('utf-8') if isinstance(v, unicode) else v) for k, v in row.iteritems()
        })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

# ================================================== #
#               Main Function                        #
# ================================================== #
def process_map(file_in, validate):
    """Iteratively process each XML element and write to csv(s)"""

    with codecs.open(NODES_PATH, 'w') as nodes_file, \
         codecs.open(NODE_TAGS_PATH, 'w') as nodes_tags_file, \
         codecs.open(WAYS_PATH, 'w') as ways_file, \
         codecs.open(WAY_NODES_PATH, 'w') as way_nodes_file, \
         codecs.open(WAY_TAGS_PATH, 'w') as way_tags_file:

        nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        validator = cerberus.Validator()

        for element in get_element(file_in, tags=('node', 'way')):
            el = shape_element(element)
            if el:
                if validate is True:
                    validate_element(el, validator)

                if element.tag == 'node':
                    nodes_writer.writerow(el['node'])
                    node_tags_writer.writerows(el['node_tags'])
                elif element.tag == 'way':
                    ways_writer.writerow(el['way'])
                    way_nodes_writer.writerows(el['way_nodes'])
                    way_tags_writer.writerows(el['way_tags'])


if __name__ == '__main__':
    # Note: Validation is ~ 10X slower. For the project consider using a small
    # sample of the map when validating.
    process_map(OSMFILE, validate=True)