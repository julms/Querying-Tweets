import sys
import csv
import datetime

samplefile = open(sys.argv[1],"rb")

reader = csv.reader(samplefile)

x = 0 #establish x and y to start loop
y = 0
first = 0
last = 0

UniqueUsers = {}

maximum = 0
for ind,row in enumerate(reader):
    maximum = ind #iterates loop until value is maximum

    t = 1 #date/time position in each row
    if y == 0: #check for first row: "==" for comparison, "=
        x = x + 1 #check for second row of data
        t = datetime.datetime.strptime(row[1],'%a %b %d %H:%M:%S %Z %Y') #row[1] = open date

    if x == 1: #created date in each row
        first = t #set current t as first and last values
        last = t
    else: #loop to establish order of dates
        if t < first:
            first = t #set lowest numbers as first until end of loop
        if t > last: 
            last = t #set highest numbers as last until end of loop
    UniqueUsers.setdefault(row[0], 0)
    
maximum += 1
first = first.strftime('%B %d %Y, %H:%M:%S') #format date and time
last = last.strftime('%B %d %Y, %H:%M:%S')

print len(UniqueUsers), "users tweeted between", first, "and", last #update wording to match assignment

samplefile.close()

