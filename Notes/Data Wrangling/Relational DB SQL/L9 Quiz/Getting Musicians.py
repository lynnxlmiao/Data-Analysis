##  Now that we know that our customers love rock music, we can decide which musicians to
##  invite to play at the concert.

##  Let's invite the artists who have written the most rock music in our dataset.
##  Write a query that returns the Artist name and total track count of the top 10 rock bands.


QUERY ='''
SELECT Artist.Name, COUNT(*) as total
FROM Genre JOIN Track
    ON Genre.GenreID = Track.GenreID
  JOIN Album
    ON Track.AlbumID = Album.AlbumID
  JOIN Artist
    ON Album.ArtistID = Artist.ArtistID
 WHERE Genre.Name = 'Rock'
 GROUP BY Artist.ArtistID
 ORDER BY total DESC
 LIMIT 10;
'''

'''
---Visual Guide---

Before Query...

#############      #############      #############      ############
#    Genre  #      #   Track   #      #   Album   #      #  Artist  #
#############      #############      #############      ############
|  GenreId  | ---> |  GenreId  |      |  ArtistId  | --->| ArtistId |
+-----------+      +-----------+      +-----------+      +----------+
|  Name     |      |  AlbumId   |---> |  AlbumId  |      |  Name    |
+-----------+      +-----------+      +-----------+      +----------+

After Query...

#######################################
#             GenreArtist             #
#######################################
|  Artist.Name  |  COUNT(Genre.Name)  |
+---------------+---------------------+

'''