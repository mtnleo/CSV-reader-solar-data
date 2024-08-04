import csv
import os

PATH = "G.csv"
DIR_LIST = []

# READ CSV
def read_csv(): 
    sum = 0

    with open(PATH, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # DELIMIT WITH COMMA ','
        next(reader)

        # GO THROUGH ALL ROWS AND GET ONLY THE NUMBER WHEN THE ROWS LOOK LIKE: Jan 1, 07:00 am,0.0449403;0.0449403
        for row in reader: 
            sum += float((row[2].split(';'))[1])
            
    return sum

def read_csv_diff():
    sum = 0

    with open(PATH, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # DELIMIT WITH COMMA ','
        next(reader)

        # GO THROUGH ALL ROWS AND GET ONLY THE NUMBER WHEN THE ROWS LOOK LIKE: "Jan 1, 07:00 am",0.276795
        for row in reader: 
            #print(row[1])
            sum += float(row[1])
            
    return sum

total_filas = read_csv_diff()
print(total_filas * 0.0321)