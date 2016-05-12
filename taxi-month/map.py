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
    clock = times[-1]
    hours = clock.split(':')
    hour = hours[0]

    if hour == 'tpep_pickup_datetime':
        continue

    if hour == '"tpep_pickup_datetime"':
        continue

    month = date_month[1]
    # hour = int(hour)

    # start_weekday = str((datetime.strptime(date, '%Y-%m-%d').weekday()))

    # if start_weekday == '0':
    #     start_weekday = 'Monday'

    # elif start_weekday == '1':
    #     start_weekday = 'Tuesday'

    # elif start_weekday == '2':
    #     start_weekday = 'Wednesday'

    # elif start_weekday == '3':
    #     start_weekday = 'Thursday'

    # elif start_weekday == '4':
    #     start_weekday = 'Friday'

    # elif start_weekday == '5':
    #     start_weekday = 'Saturday'

    # else:
    #     start_weekday = 'Sunday'

    # for i in range(len(time_interval)):
    # 	if hour >= time_interval[i][0] and hour < time_interval[i][-1]:
    #        key = 'Date:' + str(month) + ';Time Interval:' + str(time_interval[i][0]) + ',' + str(time_interval[i][-1])
    # 	   print '%s\t%s' % (key,1)
    
    key = month
    print '%s\t%s' % (key,1)




