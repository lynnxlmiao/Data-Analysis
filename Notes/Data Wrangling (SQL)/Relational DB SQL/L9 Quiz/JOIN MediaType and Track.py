## How many 'Pop' songs have an 'MPEG audio file' type?
## CREATE TABLE [MediaType]
##(
##    [MediaTypeId] INTEGER  NOT NULL,
##    [Name] NVARCHAR(120),
##    CONSTRAINT [PK_MediaType] PRIMARY KEY  ([MediaTypeId])
##);
##CREATE TABLE [Track]
##(
##    [TrackId] INTEGER  NOT NULL,
##    [Name] NVARCHAR(200)  NOT NULL,
##    [AlbumId] INTEGER,
##    [MediaTypeId] INTEGER  NOT NULL,
##    [GenreId] INTEGER,
##    [Composer] NVARCHAR(220),
##    [Milliseconds] INTEGER  NOT NULL,
##    [Bytes] INTEGER,
##    [UnitPrice] NUMERIC(10,2)  NOT NULL,
##    CONSTRAINT [PK_Track] PRIMARY KEY  ([TrackId]),
##    FOREIGN KEY ([AlbumId]) REFERENCES [Album] ([AlbumId])
##                ON DELETE NO ACTION ON UPDATE NO ACTION,
##    FOREIGN KEY ([GenreId]) REFERENCES [Genre] ([GenreId])
##                ON DELETE NO ACTION ON UPDATE NO ACTION,
##    FOREIGN KEY ([MediaTypeId]) REFERENCES [MediaType] ([MediaTypeId])
##                ON DELETE NO ACTION ON UPDATE NO ACTION
##);
##CREATE TABLE [Genre]
##(
##    [GenreId] INTEGER  NOT NULL,
##    [Name] NVARCHAR(120),
##    CONSTRAINT [PK_Genre] PRIMARY KEY  ([GenreId])
##);

QUERY = '''
SELECT Genre.Name, MediaType.Name, COUNT(*) as num 
FROM MediaType JOIN Track ON MediaType.MediaTypeId = Track.MediaTypeId 
JOIN Genre ON Track.GenreId = Genre.GenreId 
WHERE Genre.Name = 'Pop'
and MediaType.Name = 'MPEG audio file';
'''