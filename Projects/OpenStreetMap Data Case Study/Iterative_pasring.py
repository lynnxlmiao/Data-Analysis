#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pprint

OSM_PATH = "C:\Files\Udacity\Data Analyst Nanodegree\Part 4\Portland\Portland.osm"


def count_tags(filename):
    result = dict()

    for a, b in ET.iterparse(filename, events=('start',)):
        result[b.tag] = result.get(b.tag, 0) + 1
    return result


def test():
    tags = count_tags(OSM_PATH)
    print
    pprint.pprint(tags)
    print


if __name__ == "__main__":
    test()