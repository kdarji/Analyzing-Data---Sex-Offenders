__author__ = 'Krunal Darji'


import csv


with open('Sex_Offenders.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        print(row)


