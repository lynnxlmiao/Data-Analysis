# The query below finds the names and birthdates of all the gorillas.
#
# Modify it to make it find the names of all the animals that are not
# gorillas and not named 'Max'.
#

# 1
QUERY = '''
SELECT name
FROM animals 
WHERE (NOT species = 'gorilla') AND (NOT name = 'Max');
'''

# 2

QUERY = '''
SELECT name
FROM animals 
WHERE species != 'gorilla' AND name != 'Max';
'''

# 3

QUERY = '''
SELECT name
FROM animals 
WHERE NOT (species = 'gorilla' OR name = 'Max');
'''

