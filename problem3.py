import sys
import csv

samplefile1 = open(sys.argv[1], "rb")
firstreader = csv.reader(samplefile1, delimiter = ",")

firstset = set()

for row in firstreader:
    for t in row[4:]:
        firstset.add(t)

#print len(firstset)

samplefile2 = open(sys.argv[2], "rb")
secondreader = csv.reader(samplefile2, delimiter = ",")

secondset = set()

for row in secondreader:
    for t in row[4:]:
        secondset.add(t)

#print len(secondset)

thirdset = secondset.intersection(firstset)

#print len(thirdset) 

sort = sorted(thirdset)
for hashtags in sort:
    print hashtags

samplefile1.close()
samplefile2.close()
