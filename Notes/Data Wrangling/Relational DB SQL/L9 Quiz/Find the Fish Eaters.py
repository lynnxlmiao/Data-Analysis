#
# Find the names of the individual animals that eat fish.
#
# The animals table has columns (name, species, birthdate) for each individual.
# The diet table has columns (species, food) for each food that a species eats.
#

QUERY = '''
SELECT animals.name
  FROM animals JOIN diet
    ON animals.species = diet.species
 WHERE diet.food = 'fish'
'''

QUERY_OPTIONAL = '''
SELECT name
  FROM animals,diet
 WHERE animals.species = diet.species
 and diet.food = 'fish'
'''