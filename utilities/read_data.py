import csv

def getCSVdata(fileName):
    '''
    Returns: list of rows from csv file
    '''
    # empty list to store rows
    rows = []
    # open the CSV file
    dataFile = open(fileName, 'r')
    # create a CSV reader from CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows to the rows list
    for row in reader:
        rows.append(row)
    return rows