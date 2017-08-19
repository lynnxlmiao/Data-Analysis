#
# List all the taxonomic orders, using their common names, sorted by the number of
# animals of that order that the zoo has.
#
# The animals table has (name, species, birthdate) for each individual.
# The taxonomy table has (name, species, genus, family, t_order) for each species.
# The ordernames table has (t_order, name) for each order.
#
# Be careful:  Each of these tables has a column "name", but they don't have the
# same meaning!  animals.name is an animal's individual name.  taxonomy.name is
# a species' common name (like 'brown bear').  And ordernames.name is the common
# name of an order (like 'Carnivores').

QUERY = '''
SELECT ordernames.name, count(*) as num
  FROM ordernames JOIN taxonomy
    ON ordernames.t_order = taxonomy.t_order
  JOIN animals
    ON animals.species = taxonomy.name
 GROUP BY ordernames.name
 ORDER BY num DESC
'''
