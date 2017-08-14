import xml.etree.cElementTree as ET
import pprint


OSMFILE = "C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\Portland.osm"
zip_codes = []

def is_zip_code(elem):
	return (elem.attrib['k'] == "addr:postcode")

def is_Portland_zip_code(zip_code):
    if len(zip_code) == 5:
        return (int(zip_code) > 97086 and int(zip_code) < 97299)

def audit_zip_codes(zip_code):
	#The zip code of Portland is a 5 digit number in the range from 97086 to 97299
    if not is_Portland_zip_code or len(zip_code) != 5:
            zip_codes.append(zip_code)

def audit_zip(osmfile):
	for event, elem in ET.iterparse(osmfile, events=("start",)):
		if elem.tag == "node":
			for tag in elem.iter("tag"):
				if is_zip_code(tag):
					audit_zip_codes(tag.attrib['v'])
	return zip_codes

def test():
    zip_types = audit_zip(OSMFILE)
    pprint.pprint(zip_types)


if __name__ == '__main__':
    test()