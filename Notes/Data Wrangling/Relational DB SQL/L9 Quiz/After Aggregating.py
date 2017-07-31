#
# Find the one food that is eaten by only one animal.
#
# The animals table has columns (name, species, birthdate) for each individual.
# The diet table has columns (species, food) for each food that a species eats.
#

QUERY = '''
SELECT diet.food, count(*) as num
  FROM diet JOIN animals
    ON diet.species = animals.species
 GROUP BY diet.food
HAVING num = 1
'''