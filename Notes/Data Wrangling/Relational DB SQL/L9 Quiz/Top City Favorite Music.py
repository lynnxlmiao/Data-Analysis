##  It would be really helpful to know what type of music everyone likes before
##  throwing this festival.
##  Lucky for us we've got the data to find out!
##  We should be able to tell what music people like by figuring out what music they're buying.

##  Write a query that returns the BillingCity,total number of invoices
##  associated with that particular genre, and the genre Name.

##  Return the top 3 most popular music genres for the city Prague
##  with the highest invoice total (you found this in the previous quiz!)

QUERY ='''
SELECT Invoice.BillingCity, count(*) as popularity, Genre.Name
  FROM Invoice JOIN InvoiceLine
    ON Invoice.InvoiceID = InvoiceLine.InvoiceID
  JOIN Track
    ON InvoiceLine.TrackID = Track.TrackID
  JOIN Genre
    ON Track.GenreID = Genre.GenreID
 WHERE Invoice.BillingCity = "Prague"
 GROUP BY Genre.Name
 ORDER BY Invoice.BillingCity, popularity DESC
 LIMIT 3;
'''

'''
---Visual Guide---

Before Query...

###############       #################       #############      #############
#  Invoice    #       #  InvoiceLine  #       #   Track   #      #   Genre   #
###############       #################       #############      #############
|  InvoiceId  | --->  |  InvoiceId    |       |  GenreId  | ---> |  GenreId  |
+-------------+       +---------------+       +-----------+      +-----------+
|  BillingCity|       |  TrackId      |  ---> |  TrackId  |      |  Name     |  
+-------------+       +---------------+       +-----------+      +-----------+

After Query..

#######################################
#            InvoiceGenre             #
#######################################
|  BillingCity  |  COUNT(*)  |  Name  |
+---------------+------------+--------+

'''