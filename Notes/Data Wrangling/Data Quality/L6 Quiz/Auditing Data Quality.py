import codecs
import csv
import json
import pprint

CITIES = r'C:\Files\Udacity\Data-Analysis\Notes\Data Wrangling\Data Quality\L6 Quiz\cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def skip_iter(iter_variable, to_skip):
    for i in range(0, to_skip):
        iter_variable.next()
    return iter_variable

def audit_file(filename, fields):
    fieldtypes = {}

    # YOUR CODE HERE
    with open(filename,'r') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        reader = skip_iter(reader,3)

        for feature in header:
            fieldtypes[feature] = set()
        for row in reader:
            for feature in header:
                entry = row[feature].strip()
                if entry == '' or entry == 'NULL':
                    res = type(None)
                elif entry[0] == '{':
                    res = type(list())
                elif is_int(entry):
                    res = type(int())
                elif is_float(entry):
                    res = type(float())
                else:
                    res = type(str())
                fieldtypes[feature].add(res)

    return fieldtypes

def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])


if __name__ == "__main__":
    test()