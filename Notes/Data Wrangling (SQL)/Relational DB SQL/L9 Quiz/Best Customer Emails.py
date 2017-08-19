##  The customer who has spent the most money will be declared your best customer.
##  They definitely deserve an email thanking them for their patronage :)

##  Build a query that returns the person who has the highest sum of all invoices,
##  along with their email, first name, and last name.


QUERY ='''
SELECT Customer.Email, Customer.FirstName, Customer.LastName, sum(Invoice.Total) as Total
  FROM Customer JOIN Invoice
    ON Customer.CustomerID = Invoice.CustomerID
 GROUP BY Customer.CustomerID
 ORDER BY Total DESC
 LIMIT 1;
'''

'''
---VISUAL GUIDE---

Before Query...

###############         ####################   
#  Customer   #         #     Invoice      #  
###############         ####################   
|  CustomerId | = ON  = | CustomerId       |  <-----  FROM/JOIN
+=============+         +==================+  
|  FirstName  |         | Total            |  <-----  sum Total and limit
+=============+         +==================+          to highest sum
|  LastName   |    
+=============+    
|  Email      |               
+=============+

After Query...

###################################################   
#             CustomerInvoice                     #   <-----  RESULT!
###################################################   
|  Email  |  FirstName | LastName    |    Total   |
+=========+============+=============+============+

'''