#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint

OSM_PATH = "C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Singapore\Singapore.osm"

def get_user(element):
    return element.attrib['uid']


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        key = 'uid'
        if key in element.attrib:
            users.add(get_user(element))

    return users


def test():
    users = process_map(OSM_PATH)
    pprint.pprint(len(users))
    print
    print "Number of unique users: {}".format(len(users))


if __name__ == "__main__":
    test()