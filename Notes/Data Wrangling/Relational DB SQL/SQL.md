# Data and Tables #
## Aggregations ##
## How Queries Happen ##
![](http://i.imgur.com/1Gpf2lk.png)
![](http://i.imgur.com/v6v7pD5.png)
## Joining Tables ##
![](http://i.imgur.com/aPXT1BA.png)
## Set Up Local Environment ##
```C:\> cd \sqlite_windows```
```C:\> cd sqlite_windows```
```C:\sqlite_windows>sqlite3 Chinook_Sqlite.sqlite```
```sqlite>```

Use Original Files
In the previous examples, I suggested using our Resources section which contains a small package of the files you'll need. If you prefer to get the original files they can be found here.

SQLite - https://www.sqlite.org/download.html

Downloads...

Windows: sqlite-shell-win32-x86-3090200.zip
Mac: sqlite-shell-osx-x86-3090200.zip
Linux: sqlite-shell-linux-x86-3090200.zip
Chinook Database - https://chinookdatabase.codeplex.com/releases/view/55681

Once you've downloaded and organized these files you can work with them similarly to what is described above!
### Access Your Database ###
```
cd your/file/path/chinook_db
sqlite3 chinook.db
sqlite>
```
### Running some basic commands ###
You can use the .help command at any time to find details about all your new database functions.
```sqlite> .help```
Try .tables to see what tables are in your database.
```sqlite> .tables```
If you're interested in the schema of your tables the .schema command is perfect for you.
```sqlite> .schema Album```
```
CREATE TABLE [Album]
(
[AlbumId] INTEGER  NOT NULL,
[Title] NVARCHAR(160)  NOT NULL,
[ArtistId] INTEGER  NOT NULL,
CONSTRAINT [PK_Album] PRIMARY KEY  ([AlbumId]),
FOREIGN KEY ([ArtistId]) REFERENCES [Artist] ([ArtistId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE UNIQUE INDEX [IPK_Album] ON [Album]([AlbumId]);
CREATE INDEX [IFK_AlbumArtistId] ON [Album] ([ArtistId]);
```
```
CREATE TABLE [Album] <-- This is the table name, Album.

[AlbumId] <---These are your column names
[Title]       This table has 3.
[ArtistId]    AlbumId, Title, ArtistId

            INTEGER,       <---Next are the datatypes
            NVARCHAR(160),     Each column needs a datatype
            INTEGER,           You learned these last lesson!    
```
### Start Queriying your Data! ###
The Chinook database is an iTunes library representing a digital music store. We'll be getting very familiar with this database throughout these problem sets.
So now you've seen the table names in this database. Let's have a look at all the data from the Invoice table.
```sqlite> SELECT * FROM Invoice;```
Now check out what's in the Employee table.
```sqlite> SELECT * FROM Employee;```
When you're all done exploring you can .exit the database.
```sqlite> .exit```
Come back anytime using **$ sqlite3 chinook.db**.

You'll be using this dataset throughout the Problem Sets in this course.

### Select clauses ###
These are all the select clauses we've seen in the lesson so far.
*** where ***
The where clause expresses restrictions — filtering a table for rows that follow a particular rule. where supports equalities, inequalities, and boolean operators (among other things):
+ where species = 'gorilla' — return only rows that have 'gorilla' as the value of the species column.
+ where name >= 'George' — return only rows where the name column is alphabetically after 'George'.
+ where species != 'gorilla' and name != 'George' — return only rows where species isn't 'gorilla' and name isn't 'George'.

*** limit / offset ***
The *** limit *** clause sets a limit on how many rows to return in the result table. The optional *** offset *** clause says how far to skip ahead into the results. So *** limit 10 offset 100 *** will return 10 results starting with the 101st.

*** order by ***
The *** order by *** clause tells the database how to sort the results — usually according to one or more columns. So *** order by species, name *** says to sort results first by the species column, then by name within each species. Ordering happens before *** limit/offset ***, so you can use them together to extract pages of alphabetized results. (Think of the pages of a dictionary.) The optional *** desc *** modifier tells the database to order results in descending order — for instance from large numbers to small ones, or from Z to A.

*** group by ***
The ** group by ** clause is only used with aggregations, such as max or sum. Without a group by clause, a select statement with an aggregation will aggregate over the whole selected table(s), returning only one row. With a group by clause, it will return one row for each distinct value of the column or expression in the ** group by ** clause.

** Join Syntax **
Joining Tables
```
select T.thing, S.stuff
from T join S
on t.target = s.match
```
Simple Match
```
select T.thing, S.stuff
from T,S
where t.target=s.match
```
## WORKING WITH CSV's in SQLite ##
You're able to both import CSV files and export data as CSV files from SQLite.

### EXPORT DATA TO CSV FROM DATABASE ###
```
sqlite> .mode csv
sqlite> .output newFile.csv
sqlite> SELECT * FROM myTable;
sqlite> .exit
```
### IMPORT YOUR CSV INTO A TABLE ###
```
$ sqlite3 new.db   <--- If you'd like your csv's in a new database remember to make it first.

sqlite> CREATE TABLE myTable() <--- Build your schema!
sqlite> .mode csv
sqlite> .import newFile.csv myTable
```
There are a few limitations you'll come up against working this way. SQLite can't handle EVERYTHING but it's a great start!


# OSM XML #
XML is a so called meta format to provide even human readable data interexchange formats. Various file formats use this data tree structure to embedd their datas like XHTML, SVG, ODT, ...
[Wiki OSM_XML](https://wiki.openstreetmap.org/wiki/OSM_XML#JOSM_file_format)

**Pros:**
human readable because of clear structure
machine independent due to exact definitions, e.g. character sets, XML schema definitions, DTD, namespaces...
ready to use parsers for general XML that can be customized for a concrete file format
good compression ratio

**Cons:**
very huge files when decompressed
might need to decompress before processing (data compression/decompression may be performed on the fly by the transport protocol such as HTTP)
parsing may take a lot of time and memory resources, but only when using the full XML capabilities; basic XML (without DTD and namespaces) however is very fast and can be performed efficiently on the fly, without computing the DOM for the whole XML document (e.g. with simple SAX parsers)

**Contents**
+ an XML suffix introducing the UTF-8 character encoding for the file
+ an osm element, containing the version of the API (and thus the features used) and the generator that distilled this file (e.g. an editor tool)
 + a block of [nodes](https://wiki.openstreetmap.org/wiki/Node) containing especially the location in the WGS84 reference system
   + the tags of each node
 + a block of [ways](https://wiki.openstreetmap.org/wiki/Way)
   + the tags of each way
 + a block of [relations](https://wiki.openstreetmap.org/wiki/Relation)
   + the references to its members for each relation
   + the tags of each relation