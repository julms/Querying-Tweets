import sys
import csv
import datetime
import operator

samplefile = open(sys.argv[1], "rb")

reader = csv.reader(samplefile)

x = 0

TimeStamps = {}  #this is an empty dictionary, stores keys & values

for row in reader: #start of the loop
    t = datetime.datetime.strptime(row[1],'%a %b %d %H:%M:%S %Z %Y').strftime('%B %d %Y, %H:%M:%S')
    TimeStamps.setdefault(t, 0)
    TimeStamps[t]+=1

print max(TimeStamps.iteritems(), key=operator.itemgetter(1))[0], "with", max(TimeStamps.iteritems(), key=operator.itemgetter(1))[1], "tweets"

samplefile.close()
