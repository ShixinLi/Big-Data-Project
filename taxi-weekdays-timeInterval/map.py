#!/usr/bin/python

import sys
from datetime import datetime

time_interval = [[0, 7], [7, 11], [11, 15], [15, 19], [19, 24]]

for line in sys.stdin:
    
    values = line.strip().split(',')

    start_time = values[1].replace('\"', '')
    times = start_time.split(' ')
    date = times[0]
    date_month = date.split('-')
    month = date_month[0]
    clock = times[-1]
    hours = clock.split(':')
    hour = hours[0]

    if hour == 'tpep_pickup_datetime':
        continue

    elif hour == '"tpep_pickup_datetime"':
        continue

    elif hour[0] == '0':
        part_hour = hour[1]

    else:
        part_hour = hour
    part_hour = int(part_hour)

    start_weekday = str((datetime.strptime(date, '%Y-%m-%d').weekday()))

    if start_weekday == '0':
        start_weekday = 'Monday'

    elif start_weekday == '1':
        start_weekday = 'Tuesday'

    elif start_weekday == '2':
        start_weekday = 'Wednesday'

    elif start_weekday == '3':
        start_weekday = 'Thursday'

    elif start_weekday == '4':
        start_weekday = 'Friday'

    elif start_weekday == '5':
        start_weekday = 'Saturday'

    else:
        start_weekday = 'Sunday'

    for i in range(len(time_interval)):
    	if part_hour >= time_interval[i][0] and part_hour < time_interval[i][-1]:
           key = start_weekday + '; ' + str(time_interval[i][0]) + ',' + str(time_interval[i][-1])
    	   print '%s\t%s' % (key,1)




