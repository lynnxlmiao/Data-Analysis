# Data Quality #
## Measuring Data Quality ##
### Quality Metrics ###
+ Validity: conforms to a schema
+ Accuracy: conforms to gold standard
+ Completeness: all records?
+ consistency: matches other data
+ Uniformity: same units
### Blueprint for cleaning ###
+ Audit your data
+ Create a data cleaning plan
 - Identify causes
 - Define operations
 - Test
+ Execute the plan
+ Manually correct
### Example of this process: Chicago Mapzen ###
```python
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
```
```python
osm_file = open("chicago.osm", "r")
```
```python
street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
street_types = defaultdict(int)
```
```python
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()

        street_types[street_type] += 1
```
```python
def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print "%s: %d" % (k, v)
```
```python
def is_street_name(elem):
    return (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")
```
```python
def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_street_name(elem):
            audit_street_type(street_types, elem.attrib['v'])    
    print_sorted_dict(street_types)
```
```python
if __name__ == '__main__':
    audit()
```
