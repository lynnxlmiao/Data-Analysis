## Data Extraction Fundamentals ##
### Parsing CSV Files ###
```python
# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!

def parse_file(datafile):
    data = []
    with open(datafile,"rb") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break

            fields = line.split(",")
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1
    return data
```
```f.readline().split(",")``` read 1st row(header) and split.
see: https://stackoverflow.com/questions/4796764/read-file-from-line-2-or-skip-header-row
```value.strip()```Python string method strip() will come in handy to get rid of the extra whitespace (that includes newline character at the end of line).
### CSV Module ###
```import csv```
```python
with open(datafile, 'rb') as sd:
	 r = csv.DictReader(sd)
```
Read csv file as dictionary.
see: https://docs.python.org/2/library/csv.html
### Intro to XLRD ###
```python
import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col) 
                for col in range(sheet.ncols)] 
                    for r in range(sheet.nrows)]

    print "\nList Comprehension"
    print "data[3][2]:",
    print data[3][2]

    print "\nCells in a nested loop:"    
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print sheet.cell_value(row, col),


    ### other useful methods:
    print "\nROWS, COLUMNS, and CELLS:"
    print "Number of rows in the sheet:", 
    print sheet.nrows
    print "Type of data in cell (row 3, col 2):", 
    print sheet.cell_type(3, 2)
    print "Value in cell (row 3, col 2):", 
    print sheet.cell_value(3, 2)
    print "Get a slice of values in column 3, from rows 1-3:"
    print sheet.col_values(3, start_rowx=1, end_rowx=4)

    print "\nDATES:"
    print "Type of data in cell (row 1, col 0):", 
    print sheet.cell_type(1, 0)
    exceltime = sheet.cell_value(1, 0)
    print "Time in Excel format:",
    print exceltime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    print xlrd.xldate_as_tuple(exceltime, 0)

    return data

data = parse_file(datafile)
```
Looping all the column and rows data into a python list.
### Intro to JSON ###
+ Items may have different fields
+ May have nested objects
+ May have nested arrays
sources:
[W3 Schools](https://www.w3schools.com/js/js_json_intro.asp)
[Introducing JSON](http://www.json.org/)
[python's JSON module](https://docs.python.org/2/library/json.html)
Note that JSON arrays are interpreted as lists and JSON objects as dictionaires.
[Requests: HTTP for Humans](http://requests.readthedocs.io/en/latest/)
