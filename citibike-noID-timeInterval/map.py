#!/usr/bin/python

import sys

time_interval = [[0, 7], [7, 11], [11, 15], [15, 19], [19, 24]]

for line in sys.stdin:
    
    values = line.strip().split(',')

    start_id = values[3].replace('\"', '')

    start_time = values[1].replace('\"', '')
    times = start_time.split(' ')
    date = times[0]
    date_month = date.split('/')
    month = date_month[0]
    clock = times[-1]
    hours = clock.split(':')
    hour = hours[0]

    if hour == 'starttime':
        continue

    if hour == '"starttime"':
        continue

    hour = int(hour)

    for i in range(len(time_interval)):
    	if hour >= time_interval[i][0] and hour < time_interval[i][-1]:
    
            key = str(time_interval[i][0]) + ',' + str(time_interval[i][-1])
            print '%s\t%s' % (key,1)




