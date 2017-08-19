##  The show was a huge hit! Congratulations on all your hard work :)
##  After the popularity of your first show you've decided to jump on the
##  railway for an Alternative & Punk tour through France!

##  What does the alternative punk scene look like throughout French
##  cities in your dataset?

##  Return the BillingCities in France, followed by the total number of
##  tracks purchased for Alternative & Punk music.
##  Order your output so that the city with the highest total number of
##  tracks purchased is on top.


QUERY = '''
SELECT Invoice.BillingCity, count(*) as popularity
  FROM Invoice JOIN InvoiceLine
    ON Invoice.InvoiceID = InvoiceLine.InvoiceID
  JOIN Track
    ON InvoiceLine.TrackID = Track.TrackID
  JOIN Genre
    ON Track.GenreID = Genre.GenreID
 WHERE Invoice.BillingCountry = "France"
   AND Genre.Name = 'Alternative & Punk'
 GROUP BY BillingCity
 ORDER BY popularity DESC
'''


'''
---Visual Guide---

Before Query...

#################       #################       #############      #############
#    Invoice    #       #  InvoiceLine  #       #   Track   #      #   Genre   #
#################       #################       #############      #############
|  InvoiceId    | --->  |  InvoiceId    |       |  GenreId  | ---> |  GenreId  |
+---------------+       +---------------+       +-----------+      +-----------+
|  BillingCity| |       |  TrackId      |  ---> |  TrackId  |      |  Name     |  
+---------------+       +---------------+       +-----------+      +-----------+
| BillingCountry|
+---------------+

After Query..

###############################
#        InvoiceGenre         #
###############################
|  BillingCity  |  NumTracks  |
+---------------+-------------+

'''