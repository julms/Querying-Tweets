import sys
import csv
import operator

samplefile = open(sys.argv[1], "rb")

reader = csv.reader(samplefile)

lat = 0
lon = 0

NewYork = {}
SanFrancisco = {}

for row in reader: #start of the loop, checks which tweets are in New York
    if float(row[2]) > -74.2557 and float(row[2]) < -73.6895 and float(row[3]) > 40.4957 and float(row[3]) < 40.9176:

        TempList = row[4:]

        for x in TempList:
            NewYork.setdefault(x, 0)
            NewYork[x]+=1

    if float(row[2]) > -122.5155 and float(row[2]) < -122.3247 and float(row[3]) > 37.7038 and float(row[3]) < 37.8545:

        TempList = row[4:]

        for x in TempList:
            SanFrancisco.setdefault(x, 0)
            SanFrancisco[x]+=1

NewYork = sorted(NewYork.iteritems(), key=operator.itemgetter(0))
NewYork = sorted(NewYork, key=operator.itemgetter(1), reverse=True)

print "New York:"

for i in xrange(5): #for variable in the range, run "k" times
    print NewYork[i][0]+",",  NewYork[i][1]

SanFrancisco = sorted(SanFrancisco.iteritems(), key=operator.itemgetter(0))
SanFrancisco = sorted(SanFrancisco, key=operator.itemgetter(1), reverse=True)

print "San Francisco:"

for i in xrange(5): #for variable in the range, run "k" times
    print SanFrancisco[i][0]+",",  SanFrancisco[i][1]

samplefile.close()
