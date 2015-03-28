import sys
import csv
import operator

samplefile = open(sys.argv[1], "rb")

reader = csv.reader(samplefile)

x = 0
y = 0

Hashtags = {}  #this is an empty dictionary, stores keys & values

for row in reader: #start of the loop
    TempList = row[4:]
    #print TempList
    for x in TempList:
        Hashtags.setdefault(x, 0)
        Hashtags[x]+=1

#print Hashtags

Hashtags = sorted(Hashtags.iteritems(), key=operator.itemgetter(0))
Hashtags = sorted(Hashtags, key=operator.itemgetter(1), reverse=True)

for i in xrange(10): #for variable in the range, run "k" times
    print Hashtags[i][0]+",",  Hashtags[i][1]

samplefile.close()
