__author__ = 'Krunal Darji'


import csv



csvfile = 'Sex_Offenders.csv'
counter = 0
counter_non = 0

print ('Enter the race of the offender')
Race = raw_input ("Enter a race")
find = Race


#Retrieve data from CSV file

readCSV = csv.DictReader(open(csvfile, 'rb'), delimiter=',', quotechar= '"')

#Argument to see number of Female offenders and Male offenders
for line in readCSV:
    if ((line['RACE'] == find ) & (line ['GENDER'] == 'MALE')):
        counter +=1

    elif ((line['RACE'] == find ) & (line ['GENDER'] == 'FEMALE')):
        counter_non +=1

print ("TOTAL number Men Offenders: " + " " + str(counter))
print ("TOTAL number Female Offenders: " + " " + str(counter_non))










