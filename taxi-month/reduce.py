#!/usr/bin/python

#### I used similar method as WordCount from website's Hadoop MapReduce tutorial.
#### Reference:http://www.quuxlabs.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
from operator import itemgetter
import sys

counter = {}
for line in sys.stdin:
    key, value = line.strip().split('\t')

    try:
    	counter[key] = counter.get(key, 0) + 1
    except ValueError:
    	pass

sorted_counter = sorted(counter.items(), key = itemgetter(1), reverse = True)

for key, value in sorted_counter:

	print '%s\t%s' % (key, value)
