##  Let's throw a promotional Music Festival in the city with the best customers!
##  Which city have you made the most money from?

##  Write a query that returns the 1 city that has the highest sum of invoice totals.
##  Return both the city name and the sum of all invoice totals.


QUERY ='''
SELECT BillingCity, sum(Total) as InvoiceTotal
  FROM Invoice
 GROUP BY BillingCity
 ORDER BY InvoiceTotal DESC
 LIMIT 1; 
'''

'''
---VISUAL GUIDE---

Before Query...

#######################
#        Invoice      #            <--- FROM 
#######################
| BillingCity | Total |           <--- SELECT 
+-------------+-------+

After Query...

##################################   
#          Invoice               #   <-----  RESULT!
##################################   
|  BillingCity  |  sum(Total)    |
+===============+================+
|   Top City      Total Invoices |
+---------------+----------------+
'''

