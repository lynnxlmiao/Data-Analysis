from collections import defaultdict
import re

phone_type = re.compile(r'\+1\-\d{3}\-\d{3}\-\d{4}')

def audit_phone_type(phone_types, phone_number):
    m = phone_type.search(phone_number)
    if not m:
        phone_types[phone_type].add(phone_number)


phone_types = defaultdict(set)

audit_phone_type(phone_types,'+1 971 279 2787')
print phone_types