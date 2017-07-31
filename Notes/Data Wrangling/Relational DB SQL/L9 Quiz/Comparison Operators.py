#
# Find all the llamas born between January 1, 1995 and December 31, 1998.
# Fill in the 'where' clause in this query.

QUERY = '''
SELECT name 
FROM animals
WHERE species = 'llama'
AND birthdate >= '1995-01-01'
AND birthdate <= '1998-12-31'
'''